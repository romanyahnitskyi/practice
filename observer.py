from event import Event
from loger import Logger
class Observer:
    def __init__(self):
        self.__events = []
    @property
    def events(self):
        return self.__events
    def update(self,e:Event):
        Logger.log(e)