from typing import Mapping


class Strategy:
    def calculate(self, a, b):
        pass

class Addition(Strategy):
    def calculate(self, a, b):
        return a + b

class Subtraction(Strategy):
    def calculate(self, a, b):
        return a - b


class Context:
    __strategy = None

    def __init__(self, strategy):
        self.__strategy = strategy

    def do_calculate(self, a, b):
        return self.__strategy.calculate(a, b)


ctx = Context(Addition())
result = ctx.do_calculate(4, 2)
print(f'Addition： {result}')

ctx = Context(Subtraction())
result = ctx.do_calculate(4, 2)
print(f'Subtraction： {result}')

