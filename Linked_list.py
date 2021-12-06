import copy
import random
from observer import Observer
from Validation import bool_n
from event import Event
class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next




class linked_list:
    observers = []

    def add_observer(self):
        o = Observer()
        linked_list.observers.append(o)
    def delete_observer(self,o:Observer):
        linked_list.observers.remove(o)
    def notify(self,e:Event):
        for i in range(len(linked_list.observers)):
            linked_list.observers[i].update(e)
    def __init__(self):
        self.head = None
        self.length = 0
        self.for_iterator=node("smth",self.head)

    def __str__(self):
        current = self.head
        stre=''
        while (current != None):
            stre+=str(current.data)+' '
            current=current.next
        return stre

    def insert(self, data):
        new_node = node(data, None)
        self.length = self.length + 1
        if (self.head):
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            self.for_iterator = node("smth", self.head)

    def insert_pos(self, data, pos):
        if bool_n(pos):
            if pos < self.length:
                if pos!=0:
                    current = self.head
                    curr = 0
                    p_current = current
                    while curr != pos:
                        p_current = current
                        current = current.next
                        curr = curr + 1
                    new_node = node(data, current)
                    p_current.next = new_node
                else:
                    new_node=node(data,self.head)
                    self.head=new_node
                    self.for_iterator = node("smth", self.head)
                self.length=self.length+1
        else:
            print("Invalid pos type")


    def read(self, n):
        if bool_n(n):
            for i in range(n):
                bool = True
                while (bool):
                    try:
                        a = int(input())
                        bool = False
                    except:
                        print("Invalid type")
                self.insert(a)
        else:
            print("Invalid type of n")

    def generate(self, n, a, b):
        if bool_n(n):
            if a > b:
                a, b = b, a
            for i in range(n):
                self.insert(random.randint(a, b))
        else:
            print("Invalid type of n")
    def delete(self, pos):
        if bool_n(pos):
            if pos < self.length:
                if pos != 0:
                    current = self.head
                    curr = 0
                    p_current = current
                    while curr != pos:
                        p_current = current
                        current = current.next
                        curr = curr + 1
                    p_current.next=current.next
                else:
                    self.head=self.head.next
                    self.for_iterator = node("smth", self.head)
                self.length=self.length-1

    def delete_range(self, pos1,pos2):
        if bool_n(pos1) and bool_n(pos2):
            for i in range(pos1,pos2):
                self.delete(pos1)

    def min_product(self):
        if(self.length>2):
            min=self.head.data*self.head.next.data
            current=self.head
            for i in range(0, self.length - 1):
                if current.data*current.next.data<min:
                    min=current.data*current.next.data
                current=current.next
        return min

    def __iter__(self):
        return Linked_List_Iterator(self.for_iterator)

    def add_rand_elem(self,how_much,ranger):
        asa = gen_elem_from(ranger)
        for i in range(how_much):
            what=next(asa)
            self.insert(what)

def gen_elem_from(range):
    while True:
        yield random.choice(range)


class Linked_List_Iterator:
    def __init__(self,head):
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if self.current.next==None:
            raise StopIteration
        self.current=self.current.next
        return self.current.data

