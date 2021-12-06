from Linked_list import linked_list
from Menu import menu
from Menu import menu_option
from Validation import bool_n
from context import Context
from  copy import deepcopy
from observer import Observer
from event import Event
menu_list = [
    menu_option('0','exit'),
    menu_option('1','generate new list'),
    menu_option('2', 'enter new list'),
    menu_option('3', 'add element on position'),
    menu_option('4', 'delete element'),
    menu_option('5', 'my task'),
    menu_option('6', 'print using an iterator'),
    menu_option('7', 'generate elem'),
    menu_option('8', 'remove_range'),
    menu_option('9', 'generate(strategy1)'),
    menu_option('10', 'read(strategy2)'),
    menu_option('11', 'use strategy')
]
c=Context()
o=Observer()
men=menu(menu_list)
my_list=linked_list()
while True:
    print(my_list)
    men.print()
    opp=input()
    if opp == "0":
        exit(0)
    elif opp=="1":
        bool = True
        while bool:
            try:
                n = int(input("n: "))
                a = int(input("a: "))
                b = int(input("b: "))
                if bool_n(n):
                    bool = False
                else:
                    print("Invalid Type")
            except:
                print("Invalid Type")
        new_list=linked_list()
        new_list.generate(n, a, b)
        my_list=new_list
    elif opp == "2":
        bool = True
        while bool:
            try:
                n = int(input("n: "))
                if bool_n(n):
                    bool = False
                else:
                    print("Invalid Type")
            except:
                print("Invalid type.")
        new_list = linked_list()
        new_list.read(n)
        my_list=new_list
    elif opp == "3":
        bool=True
        old=deepcopy(my_list)
        while bool:
            try:
                what = int(input("what: "))
                where = int(input("where: "))
                if bool_n(where):
                    bool = False
                else:
                    print("Invalid Type")
            except:
                print("Invalid Type")
        my_list.insert_pos(what,where)
        o.update(Event('Add', old, my_list, where))

    elif opp == "4":
        bool=True
        old = deepcopy(my_list)
        while bool:
            try:
                where = int(input("where: "))
                if bool_n(where):
                    bool = False
                else:
                    print("Invalid Type")
            except:
                print("Invalid Type")
        my_list.delete(where)
        o.update(Event('Delete', old, my_list, where))
    elif opp == "5":
        print(my_list.min_product())
    elif opp=="6":
        for i in my_list:
            print(i)
    elif opp == "7":
        bool = True
        while bool:
            try:
                n = int(input("n: "))
                a = int(input("a: "))
                b = int(input("b: "))
                if bool_n(n):
                    bool = False
                else:
                    print("Invalid Type")
            except:
                print("Invalid Type")
        z=my_list.add_rand_elem(n,range(a,b))
    elif opp == "8":
        try:
            old = deepcopy(my_list)
            pos1 = int(input("pos1: "))
            pos2 = int(input("pos2: "))
            my_list.delete_range(pos1,pos2)
            o.update(Event('Delete', old, my_list, f'{pos1}-{pos2}'))
        except:
            print("Invalid Type")
    elif opp == "9":
        c.set_strategy(1)
    elif opp == "10":
        c.set_strategy(2)
    elif opp == "11":
        old = deepcopy(my_list)
        if c.strategy==1:
            n = int(input("n: "))
            a = int(input("a: "))
            b = int(input("b: "))
            where = int(input("where: "))
            my_list=c.push(my_list,n,a,b,where)
        else:
            file = input("File name")

            where = int(input("where: "))
            my_list = c.push(my_list,file,where)
        o.update(Event('Add', old, my_list, where))

    else:
        print("Code not found")