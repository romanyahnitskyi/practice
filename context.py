from strategy import *


class Context:
    def __init__(self, strategy=1):
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    def set_strategy(self, strategy):
        self.__strategy = strategy

    def push(self, *args):
        options = {
            1: ContcreteStrategyA,
            2: ContcreteStrategyB
        }
        if self.strategy in options:
            s = options[self.strategy](*args)
            return s.push()