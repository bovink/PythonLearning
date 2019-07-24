from module_import.model import student


class ClassMonitor(student.Student):

    def __init__(self, name, age, classroom):
        student.Student.__init__(self, name, age, classroom)
        self.classroom = classroom

    def print(self):
        student.Student.print(self)
        print('I\'m the monitor of classroom')
