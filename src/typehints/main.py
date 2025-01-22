#整数型の型ヒント
#引数：整数型、戻り値：文字列型
def add(num1:int, num2:int) -> str:
    #変数に型ヒント
    result:str = '足し算結果=>'
    return result + str(num1 + num2)


#文字列型の型ヒント
#引数：文字列型、戻り値：文字列型
def greet(name:str)-> str:
    return f"おはよう!{name}!"


#浮動小数点の型ヒント
#引数：浮動小数点型、戻り値：浮動小数点型
def divide(dividend:float, divisor:float) -> float:
    return dividend / divisor


#リストの型ヒント
#引数：リスト「文字列型」、戻り値：なし
def process_items(items: list[str]) -> None:
    for item in items:
        print(item)


#辞書の型ヒント
#引数：リスト「文字列型」、戻り値：辞書「文字列型、整数型」
def count_characters(word_list: list[str]) -> dict[str, int]:
    #変数に型ヒント
    count_map:dict[str,int] = {}
    for word in word_list:
        #キー：文字列、値：文字列に対応する文字数
        count_map[word] = len(word)
    return count_map


"""
呼び出し
"""

#整数型の型ヒントを使用する関数をコール
result_add = add(10, 20)
print(result_add)

#文字列型の型ヒントを使用する関数コール
greeting = greet("タロウ")
print(greeting)

#リスト型の型ヒントを使用する関数をコール
process_items(["リンゴ", "ゴリラ", "ラッパ"])

#辞書型の型ヒントを使用する関数を呼び出す
character_counts = count_characters(["apple", "amazon", "google"])
print("文字に対する文字数は=>", character_counts)