import os

# ファイルの作成
with open("shibuya/sample.txt", "w") as f: 
    f.write("This is a sample file.")

os.remove("shibuya/sample.txt")