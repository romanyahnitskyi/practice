import random


def n_bool(n):
    if type(n) is int:
        if n >= 0:
            return True
    return False


class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

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

    def insert_pos(self, data, pos):
        if n_bool(pos):
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
                self.length=self.length+1
        else:
            print("Invalid pos type")

    def print_list(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next

    def read(self, n):
        if n_bool(n):
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
        if n_bool(n):
            if type(a) is int:
                if type(b) is int:
                    if a > b:
                        temp = a
                        a = b
                        b = temp
                    for i in range(n):
                        self.insert(random.randint(a, b))
                else:
                    print("Invalid type of b")
            else:
                print("Invalid type of a")
        else:
            print("Invalid type of n")
    def delete(self, pos):
        if n_bool(pos):
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
                self.length=self.length-1

    def min_product(self):
        if(self.length>2):
            min=self.head.data*self.head.next.data
            current=self.head
            for i in range(0, self.length - 1):
                if current.data*current.next.data<min:
                    min=current.data*current.next.data
                current=current.next
        return min