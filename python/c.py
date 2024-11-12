def a(name):
    print(f"WELCOME TO C's \" KiTchen\" {name}\nHow Was your day going on {name}\nWhat could you like to have {name}")
    print("if you want to look at MENU(y) or you want to order some thing(n)")
def menu(c=0):
    print()
    print("Menu".center(10))
    print("------".center(9))
    for i,j in menu_1.items():
        print(i,j,sep=".")
    print()
    a=int(input("Enter your Option"))
    placeOrder(a)

def placeOrder(a):
    try :
        order=menu_1[a]
        print(f"your {order} will be given in 5mins\nTHANKS ❤️ ")
    except KeyError:
        print("your option is out of range")

def main():
    name=input("Can i know your Name : ")
    a(name)
    c=input()
    if c=="y" :
        menu()
        print("")
    elif c=="n":
        order=input("what could you like to order: ").capitalize()
        listI_tems=[]
        for i in menu_1.values():
            listI_tems.append(i)
        if order in listI_tems:
            print(f"your {order} will be given in 5mins\n THANKS ❤️ ")
        else:
            print(f"oop's , sorry {name} we don't have iteam today" )
            menu()
menu_1={1:"Biriyani",
        2:"Coffie",
        3:"Tea",
        4:"Milk"}


if __name__=="__main__":
    main()