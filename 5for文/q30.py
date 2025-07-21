lasts = ["加藤", "佐藤", "田中"]

for last in lasts:
    print(f"{lasts.index(last)}番の{last}です")


lasts = ["加藤", "佐藤", "田中"]

for index, name in enumerate(lasts):
    print(f"{index}番の{name}です")