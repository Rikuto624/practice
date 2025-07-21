class Person:
    nationality = "Japan"

    def say_hello(self):
        print(f"こんにちは、国籍は{self.nationality}です。")

person = Person()
person.say_hello()