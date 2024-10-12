""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################### Input, print and Numbers #####################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
'''a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))
print(a+b+c)'''

#Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.
"""name=input("Enter a name : ")
print("Hi",name)
print(f"Hi {name}")
print("Hi "+name)"""

#Write a program that takes a number and print its square.
"""a=int(input("enter a number :"))
print(a**2)
"""
#Write a program that reads the length of the base and the height of a right-angled triangle.
#and prints the area. Every number is given on a separate line
"""a=int(input("enter a number :"))
b=int(input("enter a number :"))
area=(a*b)/2
print(area)"""

#Write a program that greets the user by printing the word "Hello", 
#a comma, the name of the user and an exclamation mark after it. See the examples below.
#output Hello, Harry!
'''b=input("enter a name :")
print("Hello, "+b+"!")
print(f"Hello, {b}!")'''

#N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket?
"""a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=b//a
d=b%a
print(f"{a} students distribute {d} apples among each other\n{c} apples are remaining")
"""
#Write a program that reads an integer number and prints its previous and next numbers.

"""def previous_next():
    a=int(input("Enter your number : "))
    previous=a-1
    next =a+1
    print(f"The next number for the number {a} is {next}.\nThe previous number for the number {a} is {previous}.")
previous_next()"""

#A timestamp is three numbers: a number of hours, minutes and seconds. 
#Given two timestamps, calculate how many seconds is between them
"""a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))

hr=a*3600
min=b*60

a2=int(input("Enter a number"))
b2=int(input("Enter a number"))
c2=int(input("Enter a number"))

hr1=a2*3600
min1=b2*60

time1= hr+min+c
time2= hr1+min1+c2
print(f"The number of seconds is {time2-time1}")"""

"""def time(hr, min, sec):
    diff = hr * 3600 + min * 60 + sec
    return diff

a = int(input("Enter hours: "))
b = int(input("Enter minutes: "))
c = int(input("Enter seconds: "))
a2 = int(input("Enter hours: "))
b2 = int(input("Enter minutes: "))
c2 = int(input("Enter seconds: "))

diff1 = time(a, b, c)
diff2 = time(a2, b2, c2)

print(f"The difference in seconds is {diff2 - diff1}")
"""
"""def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

a = int(input("Enter hours: "))
b = int(input("Enter minutes: "))
c = int(input("Enter seconds: "))
time1 = time_to_seconds(a, b, c)

a2 = int(input("Enter hours: "))
b2 = int(input("Enter minutes: "))
c2 = int(input("Enter seconds: "))
time2 = time_to_seconds(a2, b2, c2)

difference = time2 - time1
print(f"The difference in seconds is {difference}")"""
#A school decided to replace the desks in three classrooms. Each desk sits two students. 
#Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively
"""def test(a,b,c):
    d=a//2+a%2+b//2+b%2+c//2+c%2
    return d
a, b, c = map(int, input("Enter three integers separated by spaces: ").split(" "))
test1=test(a,b,c)
print(test1)
"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################### Integer and float numbers ####################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Given an integer number, print its last digit.
"""a=int(input("enter a number :"))
print(a%10)

def last(a):
    return a%10

last1=last(a)
print(last1)"""

#Given a three-digit number. Find the sum of its digits.
"""inp=int(input("enter a number : "))
a=inp//100
b=inp//10%10
c=inp%10
print(a+b+c)

def sum(inp):
    a=inp//100
    b=inp//10%10
    c=inp%10
    return a+b+c
sum1=sum(inp)
print(sum1)"""


#Given a positive real number, print its fractional part.
"""a=float(input ("entea a float value : "))
c=a-int(a)
print(c)
def fractional(a):
    return a-int(a)"""

#Given a positive real number, print its first digit to the right of the decimal point.

"""a=float(input ("entea a float value : "))
#12.22*10
c=a*10
a=int(c)%10
#####or#####
a= int(a*10)%10
print(a)
"""
#A car can cover distance of N kilometers per day. 
#How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
"""import math
a=int(input("Enter the distance that car can cover per day : "))
b=int(input("Enter the distance that you want to cover  : "))

D= math.floor(b/a)
print(D)
"""
#Given the integer N - the number of minutes that is passed since midnight - 
#how many hours and minutes are displayed on the 24h digital clock?
"""n=int(input("the number of minutes :"))
h=n//60
mint=n%60
print(f"the number of hr {h}:{mint}") """      

#A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

"""def cost(a,b,c):
    D=(100*a+b)*c
    dollar=D//100
    cents=D%100
    return dollar,cents
"""
"""def angle_degree(a,b,c):
    h=(a*30+b*0.5+c*1/120)
    return h"""

#Hour hand turned by α degrees since the midnight.
#Determine the angle by which minute hand turned since the start of the current hour. 
#Input and output in this problems are floating-point numbers.

"""a=float(input("Hour hand turn by a degrees"))
def angle_min(a):
    b=(a%30*12)
    return b
b=angle_min(a)
print(b)
"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################### Conditions: if, else ########################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#Given two integers, print the smaller value.
"""a=int(input('a'))
b=int(input('b'))
smaller=""
if a<=b:
    smaller=a
else:
    smaller=b
print(smaller)
"""

#For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero
#a=int(input("enter a number : "));
"""
d=""
if a>0:
    d="1"
elif a==0:
    d="0"
else:
    d=-1
print (d)"""


"""def pne(args):
    d=""
    if args>0:
        d="1"
    elif args==0:
        d="0"
    else:
        d=-1
    return d

"""

#Given three integers, determine how many of them are equal to each other. 
#The program must print one of these numbers: 3 (if all are the same), 
#2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

"""a,b,c=map(int,input("Enter your num: ").split(" "))
if a==b==c:
    print("3")
elif a==b!=c or b==c!=a:
    print("2")
else:
    print("0")
a=2
b=4
c=4

if a==b and b==c and c==a:
    print(3)
elif a==b or a==c or b==c:
    if a==b and a!=c:
        print(2)
    else:
        print(2)
else:
    print(0)

L=[a,b,c]

s=set(l)
if len(s)==1:
    print(3)
elif len(s)==2:
    print(2)
else:
    print(0)

def l(L):
    #l=[a,s,c]
    s=set(L)
    if len(s)==1:
        return 3
    elif len(s)==2:
        return 2
    else:
        return 0
d=l(L)
print(d)"""

#Chess rook moves horizontally or vertically. 
#Given two different cells of the chessboard, determine whether a rook can go from 
#the first cell to the second in one move
"""c1,r1,c2,r2=map(int,input("Enter col1 ,col2 ,row1 ,row2: ").split(","))

if c1==c2 or r1==r2 :
    print("yes Rook can move 1 step horizontally or vertically")

else:
    print('no Rook can\'t move 1 step horizontally or vertically')
"""
#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
"""c1,r1,c2,r2=map(int,input("Enter col1 ,col2 ,row1 ,row2: ").split(","))
if (c1+r1)%2==0  and (c2+r2)%2==0:
    print("yes")
elif (c1+r1)%2!=0  and (c2+r2)%2!=0:
    print("yes")
else:
    print("no")
"""
"""x1,y1,x2,y2=map(int,input("Enter col1 ,col2 ,row1 ,row2: ").split(" "))
if x1-x2 < 2 and x2-x1 < 2 and y1-y2 < 2 and y2-y1 <2:
    print("YES")
else:
    print("NO")"""
"""def can_king_move(x1, y1, x2, y2):
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return "YES"
    else:
        return "NO"

# Input reading
x1, y1, x2, y2 = map(int, input().split())

# Output result
print(can_king_move(x1, y1, x2, y2))"""


#In chess, the bishop moves diagonally, any number of squares. 
#Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move
"""c1, r1, c2, r2 = map(int, input("Enter col1, row1, col2, row2: ").split())
if abs(c1 - c2) == abs(r1 - r2):
    print("YES")
else:
    print("NO")"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
################################################ For loop with range #########################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
"""
a=int(input("Where to start "))
b=int(input("Where to end "))
for i in range(a,b+1):
    print(i,sep=" ",end=" ")
"""
#Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.

"""a=int(input("Where to start "))
b=int(input("Where to end "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
"""
#10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
"""sum =0
for i in range(0,10):
    n=int(input("Enter"))
    sum=sum+n
print(sum)"""
"""def main():
    total = sum(map(int, [input() for _ in range(10)]))
    print(total)
main()
"""

#N numbers are given in the input. Read them and print their sum


"""n=int(input("wtha's the Nth value: "))
sum=0
for i in range(n):
    s=int(input(f"Enter your {i+1}th value: "))
    sum+=s
print(sum)"""
#n=int(input("wtha's the Nth value: "))
"""sum=0
for i in range(int(input("Enter"))):
    sum+=int(input(f"Enter your {i+1}th value: "))
print(sum)
"""
"""
n = int(input("Enter the number of inputs: "))
total = sum(map(int, [input("Enter number: ") for _ in range(n)]))
print(total)
"""


#For the given integer N calculate the following sum:
"""n=int(input(">>>"))
sum=0
for i in range(1,n+1):
    sum+=i**3
print(sum)"""
"""n = int(input(">>> "))
total = sum(i**3 for i in range(n + 1))
print(total)
"""
#In mathematics, the factorial of an integer n denoted by n! is the following product

"""n=int(input(">>>"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)"""
"""def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(fact(int(input(">>>"))))"""


"""n=int(input(">>>"))
sum=[]
for i in range(n):
    s=int(input("enter"))
    sum.append(s) 
print(sum.count(0))"""
    
#Given an integer n print the sum  1!+2!+3!+...+n!

"""n=int(input(">>>>"))
fact=1
sum=0
for i in range(1,n+1):
    fact*=i
    sum+=fact
print(sum)"""
#Ladder
"""n=int(input("Enter : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

"""
#There was a set of cards with numbers from 1 to N. 
#One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards
"""n=int(input(">>>"))
y=n*(n+1)//2
for i in range(n-1):
    x=int(input(f"Enter : "))
    y-=x
print(y)"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
################################################ Strings #####################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.
"""x=input()
x=x.count(" ")
print(x+1)"""


#Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, 
#so that the first string contains one more characther than the second). 
#Now print a new string on a single row with the first and second halfs interchanged (second half first and the first half second)

#loHel,Hello
"""s=input()
l=len(s)//2
print(s[-l:]+s[:-l])"""

#Given a string consisting of exactly two words separated by a space. 
#Print a new string with the first and second word positions swapped (the second word is printed first).
"""word_1 ,word_2 = input().split(" ")
print(f"{word_2} {word_1}")"""

#Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. 
#If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything
"""s=input()
h=s.count("f")
if s==1:
    print(s.find("f"))
else:
    print(s.find("f"),s.rfind("f"))"""

#Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. 
#If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2

"""s=input()
c=s.count("f")
result=0
if c==1:
    result=-1
elif c==0:
    result=-2
else:
    result=(s.find("f",s.find("f")+1))
print(f"{result}")"""

#Given a string in which the letter h occurs at least twice. 
#Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them
"""s=input(">>>")
print(f"{s[:s.find("h")]+s[s.rfind("h")+1:]}")"""

#Given a string in which the letter h occurs at least two times,
#reverse the sequence of characters enclosed between the first and last appearances.
"""s="habcdefgijklmnh"
print(s[:s.find("h")+1]+(s[s.find("h"):s.rfind("h")][::-1])+s[s.rfind("h")+1:])"""

#Given a string. Replace in this string all the numbers 1 by the word one.
"""s=input("Enter : ")
r=s.replace("1","one")
print(r)
"""
#Given a string. Remove from this string all the characters @
"""print(input(">>>").replace("@",""))"""

#Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.
"""s=input(">>>")
#x=s[s.find("h",s.find("h")+1):s.rfind("h")]
print(s[:s.find("h",s.find("h")+1)]+s[s.find("h",s.find("h")+1):s.rfind("h")].replace("h","H")+s[s.rfind("h"):])"""





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##################################################  list  ####################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...).

"""list_num = list(map(int,input(">>>").split(" ")))
print(*list_num[::2])
"""

#Given a list of numbers, find and print all elements that are an even number. 
#In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()

"""list_num = list(map(int,input(">>>").split(" ")))
even_list = []
for i in list_num:
    if i%2==0:
        even_list.append(i)
print(*even_list)"""
        

#Given a list of numbers, find and print all the elements that are greater than the previous element.

"""list_num = list(map(int,input(">>>").split(" ")))
pre_num = list_num[0]
print(pre_num)
grater_num=[]
for i in list_num:
    if i > pre_num:
        grater_num.append(i)
    pre_num=i
print(*grater_num)
"""
#Given a list of numbers, find and print the first adjacent elements which have the same sign. 
#If there is no such pair, leave the output blank.(-1 2 3 -1 -2)

"""list_num = list(map(int,input(">>>").split(" ")))
for i in range(1,len(list_num)):
    if list_num[i]>0 and list_num[i-1]>0 :
        print(list_num[i-1],list_num[i])
        break
    elif list_num[i]<0 and list_num[i-1]<0:
        print(list_num[i-1],list_num[i])
        break"""
############or###########
"""a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break"""

#Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors    

"""list_num = list(map(int,input(">>>").split(" ")))
count=0
for i in (1,len(list_num)-1) :
    if list_num[i-1] < list_num[i] > list_num[i+1]:
        count+=1
print(count)"""
#-9 29 -100 64 26 73 -96 28 -92 11 -14 -86 -54 -67
"""a = [int(s) for s in input().split()]
с = 0
for i in range(1, len(a)-1):
    if a[i - 1] < a[i] > a[i + 1]:
        с += 1
print(с)"""

#Given a list of numbers. Determine the element in the list with the largest value. 
#Print the value of the largest element and then the index number. 
#If the highest element is not unique, print the index of the first instance.

"""list_num = list(map(int,input(">>>").split(" ")))
grate = list_num[0]
for i in list_num:
    if i > grate:
        grate=i
print(f"{grate} {list_num.index(grate)}")
"""

#Given a list of numbers with all of its elements sorted in ascending order, 
#determine and print the quantity of distinct elements in it.

"""list_num = list(map(int,input(">>>").split(" ")))
print(len(set(list_num)))"""

#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). 
#Print the resulting list. If a list has an odd number of elements, leave the last element in place.
#40 64 -80 -98 -68 56 85 87 -68 -78
#64 40 -98 -80 56 -68 87 85 -78 -68
#2 1 4 3 5
#2 1 4 3 5

#1 2 3 4 5
"""list_num = list(map(int,input(">>>").split(" ")))
first_num=list_num[0]
new_list=[]
for i in range(0,len(list_num)):
    if i%2==0:
        new_list.append(list_num[i+1])
    else:
        new_list.append(list_num[i-1])
print(*new_list)
"""
"""list_num = list(map(int, input(">>> ").split(" ")))
new_list = []
for i in range(0, len(list_num) - 1, 2):
    new_list.append(list_num[i + 1])
    new_list.append(list_num[i])
if len(list_num) % 2 != 0:
    new_list.append(list_num[-1])
print(*new_list)
"""
"""a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
"""

#Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list.
#3 4 5 2 1
#3 4 1 2 5"
"""
list_num=[int(a) for a in input(">>>").split(" ")]
minn=list_num.index(min(list_num))
macc=list_num.index(max(list_num))
list_num[macc], list_num[minn] = list_num[minn], list_num[macc]
print(*list_num)
"""
#Given a list of numbers, find and print the elements that appear in the list only once. 
#The elements must be printed in the order in which they occur in the original list.
"""list=[int(a) for a in input(">>>").split( )]#4 3 5 2 5 1 3 5
l=[]
for i in list :#4
    if i in (list):
        if list.count(i)==1:
            l.append(i)
print(*l)"""































""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
################################################ While loop ##################################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

"""n=int(input(">>>"))
i=1
while i**2<=n:
    print(i**2)
    i+=1
"""

#Given an integer not less than 2. Print its smallest integer divisor greater than 1.
"""n=int(input(">>>"))
i=2
while i!=n:
    if n%i==0:
        break
    i+=1
print(i)"""

#For a given integer N, find the greatest integer x where 2**x
#is less than or equal to N. Print the exponent value and the result of the expression  2**x

"""n=int(input(">>>"))
x=0
r=1
while r*2<=n:
    r*=2
    x+=1
print(x,r)
"""
