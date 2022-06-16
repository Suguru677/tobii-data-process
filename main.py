from tobii_data_process import TobiiDataProcess

target_data_path = "./honzikken Data Export.tsv"

TDP = TobiiDataProcess(target_data_path=target_data_path)

TDP.data_divide()