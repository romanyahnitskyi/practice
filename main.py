from Collection import  collection
from Validation import Validation
def main_menu_print():
    print("1: print collection")
    print("2: add")
    print("3: remove")
    print("4: search")
    print("5: edit")
    print("6: sort")
    print("7: End_work")
def submenu_sort_print():
    print("1. sort by ID")
    print("2. sort by name")
    print("3. sort by iban")
    print("4. sort by bank")
    print("5. sort by payment type")
    print("6. sort by amount")
    print("7. sort by datetime")
    print("8. back to main menu ")
def submenu_edit_print():
    print("1. edit ID")
    print("2. edit name")
    print("3. edit iban")
    print("4. edit bank")
    print("5. edit payment type")
    print("6. edit amount")
    print("7. edit datetime")
    print("8. back to main menu ")
print("Input file name")
file=Validation.input_file()
my_collection=collection.read_file(file)
do_it=True
while do_it:
    main_menu_print()
    opp=Validation.input_positive_num()
    if opp==1:
        print(my_collection)
    elif opp==2:
        my_collection.add_new(file)
    elif opp==3:
        id=input("Input id")
        my_collection.remove(id,file)
    elif opp==4:
        val=input("Input string")
        print(my_collection.search(val))
    elif opp==5:
        id = input("Input id")
        submenu_edit_print()
        key=Validation.input_positive_num()
        if int(key)<8:
            my_collection.edit(id,key,file)
        if int(key)>8:
            print("Invalid key")
    elif opp==6:
        submenu_sort_print()
        key=Validation.input_positive_num()
        if int(key) < 8:
            my_collection.sort(key,file)
        if int(key)>8:
            print("Invalid key")
    elif opp==7:
        do_it=False


