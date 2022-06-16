import pandas as pd
from typing import List
from datetime import datetime, timedelta
import os


class TobiiDataProcess:
    """
    tobiiからexportされるデータを処理するモジュール

    Attributes
    -----------
    tobii_data_df : `pd.DataFrame`
        分割する前のtobiiのデータ

    """

    DELETE_COLUMNS = [
        "Recording timestamp",
        "Computer timestamp",
        "Sensor",
        "Recording start time",
    ]

    def __init__(self, target_data_path: str, groupby_column_name: str, save_folder_path: str = "./divided_data") -> None:

        self.divided_data = {}
        self.save_folder_path = save_folder_path
        self.groupby_column_name = groupby_column_name
        self.tobii_data_df = pd.read_table(target_data_path)

    def tobii_data_divide(self):
        # グループ名リスト
        df_groupby = self.tobii_data_df.groupby(self.groupby_column_name)

        for group_name, df in df_groupby:
            self.divided_data[group_name] = df

    def tobii_data_format(self, delete_columns: List = DELETE_COLUMNS, delete_stimulus_name_list: List = ["Eyetracker Calibration", "Text"]):

        for group_name, df in self.divided_data.items():
            tobii_data = df.dropna(subset="Presented Stimulus name")
            tobii_data = tobii_data[~tobii_data["Presented Stimulus name"].isin(delete_stimulus_name_list)]

            recording_start_time = tobii_data["Recording start time"].iloc[0]
            recording_start_time = datetime.strptime(recording_start_time, "%H:%M:%S.%f")
            first_rest_time = recording_start_time + timedelta(seconds=tobii_data.index[0] / 250)

            tobii_data = tobii_data.drop(delete_columns, axis=1)
            tobii_data = tobii_data.reset_index(drop=True)

            time_stamps = [None] * len(tobii_data)
            for i in range(len(tobii_data)):
                time = first_rest_time + timedelta(seconds=i / 250)
                time_stamps[i] = time.time()

            tobii_data.insert(0, "time", time_stamps)

            self.divided_data[group_name] = tobii_data

    def save(self, save_folder_path: str = "./divided_data"):

        for group_name, df in self.divided_data.items():

            save_file_name = f"{group_name}.csv"
            save_file_path = os.path.join(save_folder_path, save_file_name)
            df.to_csv(save_file_path, index=False)


def read_data(**kargs):
    return TobiiDataProcess(**kargs)
