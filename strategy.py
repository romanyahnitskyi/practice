from abc import ABC, abstractmethod
from Linked_list import linked_list, gen_elem_from
from os.path import exists


class Strategy(ABC):
    @abstractmethod
    def push(self):
        pass


class ContcreteStrategyA(Strategy):
    def __init__(self, lList: linked_list, n, a, b, index):
        self.lList = lList
        self.n = n
        self.a = a
        self.b = b
        self.index = index

    def push(self):
        asa = gen_elem_from(range(self.a, self.b))
        if self.lList.head != None:
            for i in range(self.n):
                self.lList.insert_pos(next(asa), self.index)
            return self.lList
        else:
            if self.lList.head == None:
                for i in range(self.n):
                    self.lList.insert(next(asa))
                return self.lList

class ContcreteStrategyB(Strategy):
    def __init__(self, lList: linked_list, file, pos):
        self.lList = lList
        self.file = file
        self.pos = pos

    def push(self):
        if exists(self.file):
            if self.lList.head != None:
                with open(self.file) as f:
                    for line in f:
                        t = line.split()
                        for i in t:
                            self.lList.insert_pos(i, self.pos)
                            self.pos = self.pos + 1
            else:
                if self.lList.head == None:
                    with open(self.file) as f:
                        for line in f:
                            t = line.split()
                            for i in t:
                                self.lList.insert(i)
        else:
            print("File doesn`t exist")
        return self.lList
