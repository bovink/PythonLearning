class Person():

    def __init__(self, name: str = '1', age: int = 2):
        self.name = name
        self.age = age

    def print(self):
        print("name is", self.name)
        print("age is", self.age)


class Student(Person):
    classroom = '1班'

    def __init__(self, name, age):
        Person.__init__(self, name, age)

    def print(self):
        Person.print(self)
        print('class is', self.classroom)


