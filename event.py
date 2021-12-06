class Event:
    def __init__(self,name,old,new,range):
        self.__name=name
        self.__old=old
        self.__new=new
        self.__range=range
    def __str__(self):
        return f'{self.__name}:( old list: {self.__old} , new list {self.__new} , range/pos {self.__range})'
    @property
    def name(self):
        return self.__name
    @property
    def old(self):
        return self.__old
    @property
    def new(self):
        return self.__new
    @property
    def range(self):
        return self.__range