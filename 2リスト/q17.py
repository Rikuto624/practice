numbers = [5, 0, 3, 8, -4, 9, -3, 1]

numbers.pop(0)
numbers.pop(-3)

def isEven(number):
    if number %2 == 0:
        print(f"{number}は偶数")
        return True
    else:
        print(f"{number}は奇数")
        return False
    
even_numbers = list(filter(isEven, numbers))

print("元のリスト:", numbers)
print("偶数のみのリスト:", even_numbers)