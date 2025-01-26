from pydantic import BaseModel, Field

#===========================================
# スキーマ定義
#===========================================
#登録・更新で使用するスキーマ
class InsertAndUpdateMemoSchema(BaseModel):
    # メモのタイトル。このフィールドは必須。
    # Field: SWaggerUIに表示する凡例 
    title: str = Field(...,
                       description="メモのタイトルを入力してください。最低一文字以上は必要です。",
                       examples="明日のアジェンダ", min_length=1)
    # メモの詳細説明。このフィールドは任意で入力可能。
    description: str =Field(default="",
                            description="メモの内容についての追加情報。任意で記入できます。",
                            examples="会議で話すトピック：プロジェクトの進捗状況")

# メモ情報を表すスキーマ
class MemoSchema(InsertAndUpdateMemoSchema):
    # メモの一意識別子。データベースでユニークな主キーとして使用されます。
    memo_id: int = Field(...,
                         description="メモを一意に識別するID番号。データベースで自動的に割り当てられます。",
                         example=123)
    
# レスポンスで使用する結果用スキーマ
class ResponseSchema(BaseModel):
    # 処理結果のメッセージ。このフィールドは必須。
    message: str = Field(...,
                        description="API操作の結果を説明するメッセージ",
                         example="メモの更新に成功しました。")
