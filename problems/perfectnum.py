pf=int(input("Number: "))
def main(pf):
    lis=[]
    for i in range(1,pf+1):
        if perfect_num(i):
            lis.append(i)
    return lis
def perfect_num(pf):
    l=0
    for i in range(1,pf):
        if pf%i==0:
            l+=i
    return l==pf
print(main(pf))
