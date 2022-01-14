from abc import ABC, abstractclassmethod


class Duck(ABC):

    def __init__(self):
        pass

    @abstractclassmethod
    def display(self):
        pass
    
    def performFly(self):
        self.flyBehehavior.fly()
    
    def performQuack(self):
        self.quackbehavior.quack()

    

class MallarDuck(Duck):

    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()



### FlyBehevior
class FlyBehevior(ABC):

    @abstractclassmethod
    def fly(self):
        pass

    
class FlyWithWings(FlyBehevior):

    def fly(self):
        print('飛んでいます！！')


class FlyNoWay(FlyBehevior):

    def fly(self):
        print('飛べません')

### QuackBehavior
class QuackBehavior(ABC):
    
    @abstractclassmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print('ガーガー')


class MuteQuack(QuackBehavior):

    def quack(self):
        print('<<沈黙>>')

class Squeak(QuackBehavior):

    def quack(self):
        print('キューキュー')