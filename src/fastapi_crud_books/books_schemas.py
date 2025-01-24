from pydantic import BaseModel

#書籍の作成・更新に使用するスキーマ
class BookSchema(BaseModel):
    #タイトル
    title: str
    #カテゴリ
    category: str


#レスポンス用のスキーマ
#書籍スキーマを継承。idを追加
class BookResponceSchema(BookSchema):
    #ID
    id: int
