'''
实例方法、类方法、静态方法

实例方法强制要求参数self，在调用时会自动传入实例

类方法强制要求参数cls，在调用时会自动传入类

静态方法没有强制要求参数



'''


class A():
    name = 'name'

    def printNormal(self, a):
        print('normal')
        print(self.name)

    @classmethod
    def printClass(cls):
        print('class')
        print(cls.name)

    @staticmethod
    def printStatic():
        print('static')


a = A()
# a.name = 'good'
# a.printNormal()
# a.printClass()
# a.printStatic()
#
# print('==============================')
# A.printNormal(a, '')
# A.printClass()
# A.printStatic()
A.printNormal(a,"a")
