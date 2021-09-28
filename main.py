from Linked_List import linked_list

repeat='1'
while(repeat!='0'):
    boo=1
    while(boo==1):
        try:
            n=int(input("n: "))
            boo=0
        except:
            print("Invalid type.")

    ll=linked_list()
    bool=True
    while bool:
        que=input("genereta-0,enter-1")
        if que=='1':
            bool=False
        if que=='0':
            bool=False
    if que=='1':
        ll.read(n)
    if que=='0':
        bool=True
        while bool:
            try:
                a=int(input("a: "))
                b = int(input("b: "))
                bool=False
            except:
                print("Invalid Type")

        ll.generate(n,a,b)
        print("List:")
        ll.print_list()
    print(ll.min_product())
    repeat = input("Do you want continue?(Yes - Any , No - 0) ")
