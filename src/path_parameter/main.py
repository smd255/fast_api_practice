from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User

app = FastAPI()


#ユーザーIDをパスパラメータとして受け取りユーザ情報を返すエンドポイント
#引数：ユーザーID(整数)
#戻り値：辞書型
@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    #ユーザー情報の取得
    user:Optional[User] = get_user(user_id)
    if user is None:
        #ユーザーが見つからない場合は404エラーを返す
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"user_id":user.id, "username":user.name}

