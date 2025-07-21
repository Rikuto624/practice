num = 0
if num != 0:
    print(f"10 / num ={10 / num}")
else:
    print("10 / num はエラー")

try:
    print(f"10 / num ={10 / num}")
except:
    print("エラー")