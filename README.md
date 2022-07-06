# readme-template

# install
```
pip install git+https://github.com/shichiseki/tobii-data-process
```

# Example
```python
import tobii_data_process

# 削除したい列名
DELETE_COLUMNS = [
    "Recording timestamp",
    "Computer timestamp",
    "Sensor",
    "Participant name",
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
```

# 行なったこと
- 
# 行うこと
- 瞬目処理して距離見る

# Emoji
==================== Emojis ====================  
🌱  :seedling: 初めてのコミット（Initial Commit）  
🔖  :bookmark: バージョンタグ（Version Tag）  
✨  :sparkles: 新機能（New Feature）  
🐛  :bug: バグ修正（Bugfix）  
♻️  :recycle: リファクタリング(Refactoring)  
📚  :books: ドキュメント（Documentation）  
🎨  :art: デザインUI/UX(Accessibility)  
🐎  :horse: パフォーマンス（Performance）  
🔧  :wrench: ツール（Tooling）  
🚨  :rotating_light: テスト（Tests）  
💩  :hankey: 非推奨追加（Deprecation）  
🗑️  :wastebasket: 削除（Removal）  
🚧  :construction: WIP(Work In Progress)  

# naming conventions
|種類          |命名規則|例|
|:-----------:  |:-----:|:-:|
|変数           |スネークケース            |variable_name|
|定数	       |大文字のスネークケース	|CONSTANT_NAME|
|グローバル変数  |スネークケース            |global_variable_name|
|関数          |スネークケース	          |function_name|
|関数の引数	    |スネークケース	           |function_parameter_name|
|クラス	       |パスカルケース	          |ClassName|
|インスタンス変数|	スネークケース	        |instance_variable_name|
|メソッド	    |スネークケース	           |method_name|
|パッケージ	    |スネークケース	            |package_name|
|モジュール  	|スネークケース|-|


# requirements
## インストール
```
pip install -r requirements.txt
```
## 書き出し
```
pip freeze > requirements.txt
```


# docstringの書き方
```python
from typing import Tuple

class Test():
    """
    docstingの書き方

    Attributes
    -----------
    属性名 : `str`
        属性の説明

    """

    __slots__: Tuple[str, ...] = (
        "属性名",
    )

    def __init__(self) -> None:
        pass

    def test(self) -> None:
        """
        docstringの書き方

        Parameters
        ----------
        変数名 : `int`
            変数の説明
        """
        pass


a = Test()
a.test()
```
