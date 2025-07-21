dictionary = {
    "A": "渋谷",
    "B": "陸斗",
    "C": "男性",
    "D": "茨城",
    "E": "写真",
}
print(list(dictionary.keys()))
print(dictionary.keys())

# 誤答
# if list(dictionary.values() == "男性"):
#     return True
# else:
#     return False

# print(dictionary)

if "男性" in dictionary.values():
    print(True)
else:
    print(False)

"男性" in dictionary.values()

print(dictionary)

for key, value in dictionary.items():
    print(f'{key}: {value}')