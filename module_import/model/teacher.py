from module_import.model.person import person


class Teacher(person.Person):

    def __init__(self, name, age, salary):
        person.Person.__init__(self, name, age)
        self.salary = salary

    def print(self):
        person.Person.print(self)
        print('salary is', self.salary)
