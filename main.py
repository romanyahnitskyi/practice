from Linked_list import linked_list
from Menu import menu
from Menu import menu_option
from Validation import bool_n
menu_list = [
    menu_option('0','exit'),
    menu_option('1','generate new list'),
    menu_option('2', 'enter new list'),
    menu_option('3', 'add element on position'),
    menu_option('4', 'delete element'),
    menu_option('5', 'my task')
]
men=menu(menu_list)
my_list=linked_list()
while True:
    my_list.print_list()
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
    elif opp == "4":
        bool=True
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
    elif opp == "5":
        print(my_list.min_product())
    else:
        print("Code not found")
