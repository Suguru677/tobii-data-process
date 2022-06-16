import tobii_data_process

# 削除したい列名
DELETE_COLUMNS = [
    "Recording timestamp",
    "Computer timestamp",
    "Sensor",
    "Recording name",
    "Recording start time",
    "Average calibration accuracy (mm)",
    "Average calibration precision SD (mm)",
    "Average calibration precision RMS (mm)",
    "Average calibration accuracy (degrees)",
    "Average calibration precision SD (degrees)",
    "Average calibration precision RMS (degrees)",
    "Average calibration accuracy (pixels)",
    "Average calibration precision SD (pixels)",
    "Average calibration precision RMS (pixels)",
    "Average validation accuracy (mm)",
    "Average validation precision SD (mm)",
    "Average validation precision RMS (mm)",
    "Average validation precision RMS (degrees)",
    "Average validation accuracy (pixels)",
    "Average validation precision SD (pixels)",
    "Average validation precision RMS (pixels)",
]

# 分割したいファイルのパス
target_data_path = "./honzikken Data Export.tsv"

# target_data_pathに分割したいファイルのパス、groupby_column_nameに分割する基準となる列名を指定
tdp = tobii_data_process.read_data(target_data_path=target_data_path, groupby_column_name="Recording name")

# 分割するメソッド
tdp.tobii_data_divide()

# データを整形するメソッド delete_columnsに削除したい列名のリスト、delete_stimulus_name_listに削除したい提示映像名のリストを指定
tdp.tobii_data_format(delete_columns=DELETE_COLUMNS, delete_stimulus_name_list=["Eyetracker Calibration", "Text"])

# 保存メソッド
tdp.save()
