class Person():

    def __init__(self, name: str = 'noname', age: int = 0):
        self.name = name
        self.age = age

    def print(self):
        print("name is", self.name)
        print("age is", self.age)
