from fastapi import FastAPI

#FastAPIのインスタンス
app = FastAPI() 

#Getかつエンドポイント('/')でコールされる関数
@app.get("/")
async def get_hello():
    return {"message": "Hello World"}