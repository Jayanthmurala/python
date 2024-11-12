from a import main as A
from b import main as B
from c import main as C
from d import main as D
print("Restaurents : A  B  C  D")
r=input("Select RESTAURENT's : " ).upper()
if r=="A":
    A()
elif r=="B":
    B()
elif r=="C":
    C()
elif r=="D":
    D()
else:
    print(f"RESTAURENT {r} is not open yet ")
    


