import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, select

#ベースクラスの定義
#継承先クラスをDBのテーブル構造と対応させる
Base = declarative_base()

# DBファイル作成
base_dir = os.path.dirname(__file__)
# データベースのURL
#同階層のフォルダにexample.sqlite を作成
DATABASE_URL = 'sqlite+aiosqlite:///' + os.path.join(base_dir, 'example.sqlite')

# 非同期エンジンの作成
engine = create_async_engine(DATABASE_URL, echo=True)

#非同期セッションの設定
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

#モデルの定義
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

#データベースの初期化
async def init_db():
    print("データベースの初期化を開始します。")
    async with engine.begin() as conn:
        #既存のテーブルを削除
        await conn.run_sync(Base.metadata.drop_all)
        print("既存のテーブルを削除しました。")
        #テーブルを作成
        await conn.run_sync(Base.metadata.create_all)
        print("新しいテーブルを作成しました")

# ユーザー追加関数
async def add_user(name):
    print(f"{name}をデータベースに追加します。")
    #非同期セッション開始
    async with async_session() as session:
        #1トランザクションとして開始
        async with session.begin():
            user = User(name=name)
            session.add(user)   #ユーザー情報をセッションに登録
            print(f"{name}をデータベースに追加しました。")


# ユーザー取得関数
async def get_users():
    print("データベースからユーザーを取得します。")
    async with async_session() as session:
        result = await session.execute(select(User))    #SQL select実行
        users = result.scalars().all()  # 取得データをリスト形式で返す
        print("ユーザーの取得が完了しました。")
        return users
    
async def main():
    await init_db()
    await add_user("山田")
    await add_user("田中")
    users = await get_users()
    for user in users:
        print(f"{user.id}:{user.name}")

# 非同期処理の実行
import asyncio
asyncio.run(main())