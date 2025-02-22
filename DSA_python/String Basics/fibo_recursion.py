num = int(input("Enter a num: "))

def fido(n):
    if (n < 2):
        return n
    return fido(n-1) + fido(n-2)

# print(fido(num))



def fact(n):
    if n==1:
        return n
    return fact(n-1) * n

print(fact(num))