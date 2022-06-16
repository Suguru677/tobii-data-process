# readme-template

# 行なったこと
- 
# 行うこと
- 

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
