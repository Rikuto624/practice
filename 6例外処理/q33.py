num = 0
if num != 0:
    print(f"10 / num ={10 / num}")
else:
    print("10 / num はエラー")

try:
    print(f"10 / num ={10 / num}")
except ZeroDivisionError as e:
    # ZeroDivisionError が発生した場合
    # エラー内容 (e) を出力
    print(f"エラーが発生しました: {e}")
except Exception as e:
    # その他の予期せぬエラーが発生した場合
    # エラー内容 (e) を出力
    print(f"予期せぬエラーが発生しました: {e}")

print("プログラムが終了しました。") # エラーが発生してもこの行は実行される