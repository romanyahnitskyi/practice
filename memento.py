class Memento:
    def __init__(self,state):
        self.__state=state
    @property
    def state(self):
        return self.__state