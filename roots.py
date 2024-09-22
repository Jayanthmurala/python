x,y,z = input("Enter ").split(" ")
a=int(x)
b=int(y)
c=int(z)
D=((b**2)-(4*a*c))
r1= (-b+(D)**0.5)/2*a
r2= (-b-(D)**0.5)/2*a
#r2= (-b-D)/2*a
print(r1,r2,sep=(","))


########################## USEING FUNCTIONS ##################################

a,b,c=input("Enter a nums: ").split(" ")
a=int(a)
b=int(b)
c=int(c)
def equ(a,b,c):
    D=((b**2)-4*a*c)
    r1=(-b+D**(0.5))/2*a
    r2=(-b-D**(0.5))/2*a
    return r1,r2
s=equ(a,b,c)
print(s)

