dictionary = {
    "A": "渋谷",
    "B": "陸斗",
    "C": "男性",
    "D": "茨城",
    "E": "写真",
}

print("Cは", dictionary["C"])
print("Eは", dictionary["E"])

print("Cは", dictionary.get("C"))
print("Eは", dictionary.get("E"))