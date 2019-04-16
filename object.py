class Person:
    personNum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.personNum = Person.personNum + 1

    # pass
    def sayHi(self, i=1):
        print("hello {}".format(self.name))

    def printPersonNum(self):
        print("person num is {}".format(Person.personNum))

    def printAge(self):
        print("person age is {}".format(self.age))


p = Person("lilei", 1)
p.printAge()
p.printPersonNum()

l = Person("hanm", 21)
l.printAge()
l.printPersonNum()


class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("my name is {}, i'm {}".format(self.name, self.age))


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def printSalary(self):
        print("my salary is {}".format(self.salary))


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def printMarks(self):
        print("my mark is {}".format(self.marks))


t = Teacher("hanmeimei", 25, 1300)
s = Student("lilei", 18, 30)

t.printSalary()
s.printMarks()

m = [t, s]

for item in m:
    item.tell()
