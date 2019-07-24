class QuackBehavior():

    def quack(self):
        pass


class FlyBehavior():

    def fly(self):
        pass


class QuackA(QuackBehavior):
    def quack(self):
        print('quackA')


class QuackB(QuackBehavior):
    def quack(self):
        print('quackB')


class FlyA(FlyBehavior):

    def fly(self):
        print('flyA')


class FlyB(FlyBehavior):

    def fly(self):
        print('flyB')


class Duck():

    def __init__(self):
        self.quackBehavior = QuackBehavior()
        self.flyBehavior = FlyBehavior()

    def setQuackBehavior(self, quackBehavior):
        self.quackBehavior = quackBehavior

    def setFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior

    def performQuack(self):
        self.quackBehavior.quack()

    def performFly(self):
        self.flyBehavior.fly()


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self.quackBehavior = QuackA()
        self.flyBehavior = FlyA()

m = MallardDuck()

m.performQuack()
m.performFly()

m.setFlyBehavior(FlyB())
m.performFly()
