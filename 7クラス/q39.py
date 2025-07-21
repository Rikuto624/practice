class Person:
    nationality = "Japan"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"こんにちは、国籍は{self.nationality}です。")

    def say_my_name(self):
        print(f"{self.name}です。")


person = Person("渋谷")
person.say_hello()
person.say_my_name()