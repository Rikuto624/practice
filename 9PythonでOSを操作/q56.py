import os

# PATH環境変数の値を取得して表示
path_variable = os.environ.get('PATH')

if path_variable:
    print(f"PATH環境変数の値: {path_variable}")
else:
    print("PATH環境変数は設定されていません。")

print(f"次のやつ\n{os.environ['PATH']}")