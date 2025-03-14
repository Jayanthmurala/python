r=7
for i in range(r-1):
    for j in range(r-i-1):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()

for i in range(r):
    for j in range(i):
        print(" ",end=" ")
    for k in range(r*2-1-2*i):
        print("*",end=" ")

    print()
    
    