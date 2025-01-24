from fastapi import FastAPI, HTTPException
from books_schemas import BookSchema, BookResponceSchema


app = FastAPI()


#デモ用のデータベース代わりに使うリスト
#ダミーの書籍情報リスト
books: list[BookResponceSchema] = [
    BookResponceSchema(id=1, title="Python入門", category="technical"),
    BookResponceSchema(id=2, title="はじめてのプログラミング", category="technical"),
    BookResponceSchema(id=3, title="すすむ巨人", category="comics"),
    BookResponceSchema(id=4, title="DBおやじ", category="comics"),
    BookResponceSchema(id=5, title="週刊ダイヤモンド", category="magazine"),
    BookResponceSchema(id=6, title="ザ・社長", category="magazine")
]


#-----------------------------------------
#書籍を追加するためのエンドポイント
#引数：BookSchema
#戻り値：BookResponceSchema
#-----------------------------------------
@app.post("/books/", response_model=BookResponceSchema)
def create_book(book: BookSchema):
    #書籍IDを作成
    new_book_id = max([book.id for book in books], default=0) + 1
    #新しい書籍を作成
    # model_dump()は辞書型でフィールドを返す(BaseModelメソッド)
    # **は辞書の各要素を個別に渡す(アンパック)
    new_book = BookResponceSchema(id=new_book_id, **book.model_dump())
    #ダミーデータに追加
    books.append(new_book)
    #登録書籍データを返す
    return new_book


#-----------------------------------------
#書籍情報を全件取得するエンドポイント
#引数：なし
#戻り値：BookResponceSchemaのリスト
#-----------------------------------------
@app.get("/books/", response_model=list[BookResponceSchema])
def read_books():
    #すべての書籍を取得
    return books


#-----------------------------------------
#書籍情報をidによって1件取得するエンドポイント
#引数：書籍ID
#戻り値：BookResponceSchema
#-----------------------------------------
@app.get("/books/{book_id}", response_model=BookResponceSchema)
def read_book(book_id: int):
    #IDに対応する書籍情報を取得
    for book in books:
        if book.id == book_id:
            return book
    #無ければ例外を投げる
    raise HTTPException(status_code=404, detail="Book not found")
    

#-----------------------------------------
#idに対応する書籍情報を更新するエンドポイント
#引数：
#   書籍ID
#   BookSchema
#戻り値：BookResponceSchema
#-----------------------------------------
@app.put("/books/{book_id}", response_model=BookResponceSchema)
def update_book(book_id: int, book: BookSchema):
    #特定のIDの書籍を更新
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            update_book = BookResponceSchema(id=book_id, **book.model_dump())
            books[index] = update_book
            return update_book
    #無ければ例外を投げる
    raise HTTPException(status_code=404, detail="Book not found")


#-----------------------------------------
#idに対応する書籍情報を削除するエンドポイント
#引数：
#   書籍ID
#戻り値：BookResponceSchema
#-----------------------------------------
@app.delete("/books/{book_id}", response_model=BookResponceSchema )
def delete_book(book_id: int):
    # 特定IDの書籍を削除
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
    #無ければ例外を投げる
    raise HTTPException(status_code=404, detail="Book not found")
