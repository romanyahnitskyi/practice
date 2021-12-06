from memento import Memento
class CareTaker:
    def __init__(self,obj):
        self.__obj=obj
        self.__states=[]
        self.__index=-1
    @property
    def index(self):
        return self.__index
    @property
    def obj(self):
        return self.__obj
    def save(self):
        if self.index<len(self.__states)-1:
            for i in range(len(self.__states)-self.index):
                self.__states.pop()
        self.__states.append(self.obj.save_state())
        self.__index+=1
    def undo(self,file):
        if self.index<0:
            try:
                self.obj.backup(self.__states[0])
            except:
                print("No states to undo")
        else:
            if self.__index!=0:
                self.__index-=1
            self.obj.backup(self.__states[self.index],file)
    def redo(self,file):
        if self.index>=len(self.__states)-1:
            print("No states to redo")
            return None
        self.__index+=1
        self.obj.backup(self.__states[self.index],file)
    def print(self):
        for i in self.__states:
            print(i.state.__str())