def a(name):
    print(f"WELCOME TO B's \" KiTchen\" {name}\nHow Was your day going on {name}\nWhat could you like to have {name}")
    print()
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

menu_1={1:"Biriyani",
        2:"Coffie",
        3:"Tea",
        4:"Milk",
        5:"water"}

def call():
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
        else:
            print("choose : y/n")
            c = input().strip().lower()
            call(c)
            
            
def main():
    global name
    name=input("Can i know your Name : ").capitalize()
    a(name)
    c=input().strip().lower()
    call(c)
            
           
if __name__=="__main__":
    main()