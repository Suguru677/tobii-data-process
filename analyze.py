import glob
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def convert_datetime(input_dataframe: pd.DataFrame):

    times = input_dataframe["time"].tolist()
    datetimes = [datetime.strptime(time, "%H:%M:%S.%f") for time in times]
    
    input_dataframe = input_dataframe.drop("time", axis=1)
    input_dataframe.insert(0, "time", datetimes)

    return input_dataframe

def distance_analyze(target_file_path: str):

    tobii_data = pd.read_csv(target_file_path)
    
    tobii_data = convert_datetime(tobii_data)

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    SCREEN_CENTER_WIDTH = SCREEN_WIDTH / 2
    SCREEN_CENTER_HEIGHT = SCREEN_HEIGHT / 2

    point_x = tobii_data["Gaze point X"].to_list()
    point_y = tobii_data["Gaze point Y"].to_list()

    data_num = len(point_x)
    distances = [None] * data_num
    distance_diff = [float("nan")] * data_num

    distance_min = float("inf")
    distance_max = -float("inf")
    for i in range(data_num):
        x, y = point_x[i], point_y[i]
        distance = ((SCREEN_CENTER_WIDTH - x) ** 2 + (SCREEN_CENTER_HEIGHT - y) ** 2) ** 0.5
        distances[i] = distance

        distance_max = max(distance_max, distance)
        distance_min = min(distance_min, distance)

    distances = [(distance - distance_min) / (distance_max - distance_min) * 100 for distance in distances]

    diff_min = float("inf")
    diff_max = -float("inf")
    for i in range(1, data_num - 1):

        diff = (distances[i] - distances[i - 1]) / 0.004
        distance_diff[i] = diff
        diff_min = min(diff_min, diff)
        diff_max = max(diff_max, diff)

    distance_diff = [(diff - diff_min) / (diff_max - diff_min) * 100 for diff in distance_diff]

    return tobii_data, distances, distance_diff

def real_time_questionnaire(target_file_path: str):
    questionnaire_data = pd.read_csv(target_file_path)

    questionnaire_data = convert_datetime(questionnaire_data)

    return questionnaire_data

file_paths = glob.glob("./divided_data/*.csv")

for file_path in file_paths[0:1]:
    print(file_path)
    tobii_data, distances, distance_diff = distance_analyze(file_path)

questionnaire_data = real_time_questionnaire("./Real_Time_Questionnaire/ZNPV1.csv")

plt.plot(questionnaire_data["time"], questionnaire_data["distance"])
plt.plot(tobii_data["time"], distances)
plt.show()