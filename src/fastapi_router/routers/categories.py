from fastapi import APIRouter
from schemas.category import Category

router = APIRouter()

#----------------------------------------------------
# カテゴリ一覧を表示するためのエンドポイント
#----------------------------------------------------
@router.get("/categories/", response_model=dict)
async def read_categories():
    # 実際にはデータベースから取得する処理が入る予定
    return {"message": "カテゴリ一覧を表示", "categories":[]}


#----------------------------------------------------
# カテゴリを登録するためのエンドポイント
#----------------------------------------------------
@router.post("/categories/", response_model=dict)
async def create_category(category: Category):
    #実際にはデータベースから取得する処理が入る予定
    return {"message": "カテゴリを作成しました", "category":category}

#----------------------------------------------------
# カテゴリを更新するためのエンドポイント
#----------------------------------------------------
@router.put("/categories/{category_id}", response_model=dict)
async def update_create_category(category_id: int, category: Category):
    #実際にはデータベースを更新する処理が入る予定
    return {"message": "カテゴリを更新しました", 
            "category_id": category_id ,"category": category}

#----------------------------------------------------
# カテゴリを削除するためのエンドポイント
#----------------------------------------------------
@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    #実際にはデータベースを削除する処理が入る予定
    return {"message": "カテゴリを削除しました", "category_id": category_id }
