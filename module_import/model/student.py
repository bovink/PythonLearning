from module_import.model.person import person


class Student(person.Person):

    def __init__(self, name, age, classroom):
        person.Person.__init__(self, name, age)
        self.classroom = classroom

    def print(self):
        person.Person.print(self)
        print('class is', self.classroom)
