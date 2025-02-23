def num(n):
    if n ==0:
        return 0
    num(n-1)
    print(n) 

# num(5)

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
# print(fact(500))

def fido(n):
    if n ==1:
        return 1
    if n==0:
        return 0
    return fido(n-2) + fido(n-1)
print(fido(10))