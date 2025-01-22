from typing import Optional

#ユーザークラス
class User:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name


#ユーザーリストのダミーデータ
user_list = [
    User(id=1, name="内藤"),
    User(id=2, name="辻"),
    User(id=3, name="鷹木")
]


#指定されたIDに対応するユーザーを検索する関数
#引数：ユーザID(整数)
#戻り値：UserオブジェクトまたはNone(見つからない場合)
def get_user(user_id:int)->Optional[User]:
    for user in user_list:
        if user.id == user_id:
            return user

    return None     #ユーザが見つからない場合はNoneを返す