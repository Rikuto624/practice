class Person:
    nationality = "Japan"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"こんにちは、国籍は{self.nationality}です。")

    def say_my_name(self):
        print(f"{self.name}です。")

class Kid(Person):
    
    def my_age(self, age):
        print(f"{self.name}です。年齢は{age}です。")


kid = Kid("渋谷")
kid.my_age(23)
print(kid.nationality)
print(kid.name)