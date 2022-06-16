import pandas as pd
import glob

class TobiiDataProcess:
    """
    tobiiからexportされるデータを処理するモジュール

    Attributes
    -----------
    tobii_data_df : `pd.DataFrame`
        分割する前のtobiiのデータ

    """

    def __init__(self, target_data_path:str, save_folder_path: str="./divided_data") -> None:
        self.tobii_data_df = pd.read_table(target_data_path)

    def data_divide(self):
        # グループ名リスト
        self.group_list = [*self.tobii_data_df.groupby("Recording name").groups]

