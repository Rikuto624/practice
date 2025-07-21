def divide(a, b):
    try:
        print(f"計算結果：{a / b}")
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

divide(2, 0)
divide(2, 1)
divide("あ", 5)