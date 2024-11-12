"""num=int(input("enter a number"))
#nums=int(input("enter a number"))
#print("sum:",num+nums,sep="")
#print(f"sum:{num+nums}")
area = 3.14*num**2
print("area of the circle:",area,sep="")
print(f"area of the circle:{area}")
#
"""
############## SWAP THE VALUS (USING TEMP)##################
"""a=20
b=10
temp=a
a=b
b=temp
print(a)
print(b)
print(temp)
"""
# largest amount three numbers
"""a,b,c=input("enter :").split(" ")
a=int(a) 
b=int(b) 
c=int(c)

largest=""
if a >= b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else :
    largest=c
print(f"{largest} is largest number ")"""
"""
a=float(input(" enter a temp : "))
b=input("Enter the units : ").lower()

if b=="c":
    F = a*(9/5)+32
    k=(a+273)
    print(f"temp in f {F}\ntemp in k {k}")
elif b=="f":
    C=a*(5/9)-32
    k=(a+273)
    print(f"temp in c {C}\ntemp in k {k}")
elif b=="k":
    C=(a-273)
    F=(a*(9/5)+32)
    print(f"temp in f {F}\ntemp in c {C}")

"""
"""a=int(input(" enter"))
b=int(input(" enter"))
def sum(a=1,b=1):
    return a+b
j=sum(a,b)
print(j)"""

"""def area (r):
    return 3.14*r**2
r=int(input("area : "))
a=area(r)
print(a)"""

"""a,b,c=input("Enter a nums: ").split(" ")
a=int(a)
b=int(b)
c=int(c)
def equ(a,b,c):
    D=((b**2)-4*a*c)
    r1=(-b+D**(0.5))/2*a
    r2=(-b-D**(0.5))/2*a
    return r1,r2
s=equ(a,b,c)
print(s)"""


############# THE MIN  AND MAX NUMBERS OF LIST (USING ACCADING AND DECADING ORDER )###################


"""a=input("Enter a nums: ").split(" ")
print(a)
a=[int(a)for a in a]
a.sort()
l=sorted(a)
print(a)
#print(l)
print(f"the mimnum num is :{a[0]}")
print(f"the maxmum num is :{a[-1]}")
print(f"the maxmum num is {max(l)}\nthe mimnum num is {min(l)}")"""



"""l= [0,1,2,3,4,5,6,7,7,0,1,5,6]
s=set(l)

l2=list(s)
print(l2)"""
"""from snakify import last
k=int(input("Enter"))
k=last(k)
print(k)
"""
"""print(123//10)

from snakify import fractional
a=float(input("Enter"))
print(fractional(a))
"""
"""from snakify  import cost
a=int(input("The total dollars : "))
b=int(input("The total cents : "))
c=int(input("The total toys : "))
d,c=cost(a,b,c)
print(d,c)"""
"""from snakify import pne
a=int(input("the total cost"))"""
"""b=int(input("the total cost"))
c=int(input("the total cost"))

d=angle_degree(a,b,c)
print(d)"""
"""sum=0
for i in range(5,11):
    sum+=i
print(sum)
"""
#print(pne(a))

"""def main():
    n=int((input()))
    n=str(n)
    print(palindrome(n))
    

def palindrome(j):
    
    if j==j[::-1]:
        return "true"
    else:
        return "false"
main()  
"""

#swecha
"""def main():
    n=input()
    print(length(n))
def length(n):
    sum=0
    for i in n:
        if i==i:
            sum+=1
    return sum
if __name__=="__main__":
     main()
     """


"""l=map(int,input((">>")).split(" "))
l=list(l)
x=l[0]
while l:
    for i in l:
        if i >x:
            x=i
    break
j=l.index(x)
print(j+1)
"""
"""
 Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase,
and every odd letter is lowercase. Assume that the incoming string only contains letters, 
and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, 
so long as letters alternate throughout the string.

Remember, don't run the function, simply provide the definition.

To give an idea what the function would look like when tested:

print(len(myfunc('Anthropomorphism')))
# Output: 'aNtHrOpOmOrPhIsM'
Added note: this exercise requires that the function return a string. Print statements will not work here."""
"""def mystr(x):
    result = ""
    for i in range(len(x)):
        if i % 2 == 0:
            result += x[i].lower()
        else:
            result += x[i].upper()
    return result

r = mystr(input(">>>"))
print(r)
"""
"""LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5"""
"""def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
p=lesser_of_two_evens(2,5)
print(p)"""

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False"""
"""def animal_crackers(a):
    w1,w2=a.split(" ")
    if w1[0]==w2[0]:
        return True
    else:
        return False
print(animal_crackers('Levelheaded jlama'))
"""
"""MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False"""

"""def makes_twenty(a,b=0):
    if a+b==20:
        return True
    elif 20 in (a,b):
        return True
    else:
        return False
print(makes_twenty(1,20))
"""
"""OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 old_macdonald('macdonald') --> MacDonald"""
"""def old_macdonald(name):
    n1=name[:3]
    n2=name[3:]
    n1=n1.capitalize()
    n2=n2.capitalize()
    return n1+n2
print(f"{old_macdonald('macdonald')}")
"""

"""MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'"""

"""def master_yoda(lit):
    lit=lit.split(" ")
    return " ".join(lit[::-1])
print(master_yoda('We are ready'))"""

"""ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True"""
"""def almost_there(a):
    if abs(100-a)<=10 or abs(200-a)<=10:
        return True
    else:
        return False
print(almost_there(137))"""


"""Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""
"""def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False  
print(has_33([3, 1, 3]))  """   

"""PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"""

"""def paper_doll(str):
    result=""
    for i in str:
        result+=i*3
    return result
print(paper_doll('Mississippi'))"""

"""BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19"""
"""def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
def blackjack(a,b,c):
    if sum(a,b,c)<=21:
        return sum(a,b,c)
    elif 11 in (a,b,c):
        if sum(a,b,c) -10 <=21:
            return sum(a,b,c)-10
    else:
        return "BUST"
print(blackjack(9,9,11))"""

"""SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14"""

"""def summer_69(nums):
    if 6 in nums and 9 in nums:
        return sum(nums) - (sum(nums[nums.index(6):nums.index(9)+1]) or sum(nums[nums.index(9):nums.index(6)+1]))
    else:
        return sum(nums)

print(summer_69([2, 1, 6, 9, 11]))  # Output: 9"""

"""SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""
""""def spy_game(num):
    l=[]#007
    for i in num:
        if i == 0 or i==7:
            l.append(i)
    if l==[0,0,7]:
        return True
    else:
        return False
print(spy_game([1,7,2,0,4,5,0]))     
            """
        


"""Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as
"""
"""def vol(r):
    return ((4/3)*(3.14)*(r**3))
print(vol(2))"""

"""Write a function that checks whether a number is in a given range (inclusive of high and low)"""

"""def ran_check(num,start,end):
    if num in range(start,end+1):
        return True
    else: return False
print(ran_check(5,2,7))"""

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()"""

"""def up_low(str):
    upper=0
    lower=0
    for check in str:
        if check.isupper()==True:
            upper+=1
        elif check.islower()==True:
            lower+=1
    print(f"No. of Upper case characters : {upper}\nNo. of lower case characters : {lower}")
up_low(input(">>>"))"""

"""Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24"""
"""def mul(num):
    result=1
    for i in num:
        result*=i
    return result
print(mul([1, 2, 3, -4]))   """


"""Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""
"""import string

def pangram(str, str1=string.ascii_lowercase):
    str = str.replace(" ", "").lower()
    for char in str1:
        if char not in str:
            return False
    return True

print(pangram("The quick brown fo jumps over the lazy dog"))"""
"""def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))

        if board[row][col] != ' ':
            print("Cell already taken, try again.")
            continue
        
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()

"""









"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn

"""
"""class Account:
    def __init__(self, owner:str, blance:int)->None:
        self.owner = owner
        self.blance = blance
    def __str__(self) -> str:
           return f'Account owner:{self.owner}\nAccount balance: ${self.blance}'
    def check(self):
           print(f"You have {self.blance} in your Account!")
    def deposit(self,add):
                self.blance +=add
                print (f"You have add {add} To Your Account! ")
                return self.blance
    def withdraw(self,sub):
           if sub > self.blance:
                print("The fund is insafficent plz Recheck your Account Blance!")
                return None
           else:
                  self.blance-=sub
                  print(f"You have withdrawn {sub}. Remaining balance: {self.blance}\nTHANK YOU🤝")
                  return self.blance
acc=Account("Jayanth",100)
print(acc)
acc.check()
acc.deposit(100)
acc.check()
acc.withdraw(100)
acc.withdraw(200)"""


#Handle the exception thrown by the code below by using try and except blocks.
"""try:
    for i in ["a","b","c"]:
        print(i*2)
except TypeError:
    print("somthing went wrong")
else:
    print("now it's fine")
"""
#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
"""try:
    x = 5
    y = 0
    z = x/y
except:
    print("it's zeroerror check your division")
finally:
    print("All Done")"""


#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

"""def ask()->int:
    while True:
        try:
            j=int(input("Input an integer: "))
            print(f"Thank you, your number squared is: {j*j}")
            break
        except:
            print("An error occurred! Please try again!")
ask()"""



"""for i in range(1,int(input())+1): 
    print ((1111111111 % (10 ** i)) ** 2)



print(1111111111 % 1000)
"""
""""from math import gcd
len_of_list=int(input()) #[29 14 7 6 25]
array=list(map(int,input().split()[:len_of_list]))
def coprimes(array):
    uniqe_array=list(set(array))
    count_pair=0
    for i in range(len(uniqe_array)):
        for j in range(i+1,len(uniqe_array)):
            if gcd(uniqe_array[i],uniqe_array[j])==1:
                count_pair +=1
    return count_pair
print(coprimes(array))
"""

"""
string=input()
for i in range(len(string)-1):
    if string[i+1]==string[i]:
        string=string.replace(string[i+1],"")

        
print(string)"""

"""a=8
a%=float(1)
print(a)
#print(b)"""





"""age=int(input("Give me your age: "))
a="pencli"#1-10 age
b="pen"#11-20
c="book"#21......
result=""
if 1<age & age<=10:
    result=a
    print("Take",result)
elif  11<age<=20:
    result=b
    print("Take",result)
elif 21<age:
    result=c
    print("Take",result)
else:
    print("rechek your input")"""



"""a=10;
while a>=0:#true when the j=10 it  com's out of the loop
    print("take this",a);
    a-=1;"""

"""for i in range(0,10+1):#(start,end,step)
    print("2 *",i,"=" ,2*i)
"""
"""box=10
check=0
while check>=10:
    print("take: ",check)"""
    

"""taking_input=input("sir plz Enter your name : ")
print(taking_input)
print(type(taking_input))
"""


"""num=float(input("Enter some num : "))
print(num)
print(type(num))"""


"""j="jayanth"#[start:stop:step]
k=j[-5:]
k=k[::-1]
print(k)
"""

"""You are given a string.
In the first line, print the third character of this string.

In the second line, print the second to last character of this string.

In the third line, print the first five characters of this string.

In the fourth line, print all but the last two characters of this string.

In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).

In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

In the seventh line, print all the characters of the string in reverse order.

In the eighth line, print every second character of the string in reverse order, starting from the last one.

In the ninth line, print the length of the given string."""


"""s="1234567890"
print(s[2])
print(s[1:])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[::3])
print(s[::-1])
print(s[-1::-2])"""


"""for i in range(10):
    if i==5:
        continue
    print(i)"""
"""
l=[1,"j",9,"jayanth",8754,3.24,1,1]

print(l[3])"""


"""def sum(a,m):
    print(a+m)
sum(10,20)

ak=lambda a,b : a+b
print(ak(10,20))
"""


"""i=[1,2,3,4,5,5,5,6,6,7,8,"ghdsv"]
j=set(i)#{1,2,3.....}
print(i[0])
print(j)
"""

#D={"name":"j",
"""   1:"a",
   2:"y"
}

for k in D.items(): #1,a
    print(k)
"""

myfamily = {
  "child1" : {"name" : "Emil","year" : 2004,"age":99},
  "child2" : {"name" : "Tobias","year" : 2007,"age":6},
  "child3" : {"name" : "Linus","year" : 2011,"age":5}
}
l=[]
k=[]
j=[]
"""for k in myfamily.values():
    for i in k.keys():
        #print(i)
        if i=="year":
           l.append(k[i])
print(l)
    """

# for i in myfamily:
#     l.append(myfamily[i]["name"])
#     j.append(myfamily[i]["year"])
#     k.append(myfamily[i]["age"])
# print(l,j,k)

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

"""num_ary=list(map(int,input(">").split(",")))
target=int(input(">"))

for i in range(len(num_ary)-1):
    for j in range(i+1,len(num_ary)):
        if (num_ary[i])+(num_ary[j])==target:
            print(f"[{i},{j}]")
"""
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500     XII ,III
# M             1000

# # Test cases


# class Solution:
#     def roman(self,s:str)->int:
#         count=0
#         D={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         for i in range(len(s)):
#             if i < len(s) - 1 and D[s[i]] < D[s[i + 1]]:
#                 count -= D[s[i]]
#             else:
#                 count += D[s[i]]
        
#         return count
# d=Solution()
# dd="iv".upper()
# print(d.roman(dd))
# print(d.roman("III"))      # Output: 3 (Correct)
# print(d.roman("IV"))       # Output: 6 (Incorrect, should be 4)
# print(d.roman("IX"))       # Output: 11 (Incorrect, should be 9)
# print(d.roman("LVIII"))    # Output: 58 (Correct)
# print(d.roman("MCMXCIV"))  # Output: 2116 (Incorrect, should be 1994)
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

# strs = ["flower","flow","flight"]

# for i in range(len(strs)):
#     l=strs[i]
#     for j in l:



# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
"""g="jayanth"
print("g.pop(1)")
"""
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
# def solution(num):
#     ans=[]
#     for i in num:
#         ans.append(num[i])
#     return ans
# print(solution(nums))
# print(nums)


""""class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(nums[i])
        return ans
        
nums = [5, 0, 1, 2, 3, 4]
solution = Solution()  
result = solution.buildArray(nums)"""

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
"""nums = [1,2,1]
ans=[]
for i in range(2):
    for j in nums:
        ans.append(j)
print(ans)
"""


# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# nums=[1,2,3,4]
# sum=0
# n=[]
# for i in range(len(nums)):
#     sum+=nums[i]
#     n.append (sum)    
# print(n)
""""""
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6
"""
accounts = [[2,8,7],[7,1,3],[1,9,5]]
#print(sum(accounts[1]))
l=[]
for i in range(len(accounts)):
    j=sum(accounts[i])
    l.append(j)
print(max(l))
    """

# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:

# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:

# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
# nums = [2,5,1,3,4,7]
# n=3
# xl=nums[:n]
# y1=nums[n:]
# n=[]
# for i in range(len(nums)//2):
#     m=xl[i],y1[i]
#     n.append(m)
#     n.append(y1[i])

# print(xl)
# print(y1)
# print(n)

# def evenchek(j):
#     sum=0
#     if(j>9):
#         for i in str(j):
#             sum+=int(i)
#     return sum
# print(evenchek(12))
""""xor gate"""
# print(0^0)
# print(9^10)#1001,1010=0011. 0001,1010=1011
# print(0^1)
# print(1^1)

""""xor to find non dublicet ele"""
# c=0
# for i in [2,-2,3,4,6,-4,3]:
#     print("inside befor ",c,i)
#     c^=i
#     print("inside after ",c)
# print(c)

""""Even or odd using & gate"""
# for i in range(10):
#     if(i&1==1):
#         print(f"{i} is odd")
#     else:
#         print(f"{i} is even ")

# def num(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1

#     else:
#         return num(n-2)+num(n-1)
# print(num(5))
"""nth bit in binary"""
# n=int(input(">>>: "))
# ans=0
# base=int(input(">>>: "))
# temp=base
# while(n>0):
#     lastBit=n&1
#     n>>=1
#     ans+=lastBit*base
#     base*=temp
# print(ans)
import math
"""num of digits in binary'2' and base'10'"""
        #    """for binary"""
# num=7
# base=2
# print(math.ceil(math.log(num)/math.log(base)))

# decimal
# num=12345678
# base=10
# print(math.ceil(math.log(num)/math.log(base)))
""""""
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

 

# Example 1:

# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# Example 2:

# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
# minJump = 2
# maxJump = 3
# s = "01101110"
# print(s[-(minJump+maxJump+1)]=="0")

# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
# Example 1:
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.
"""s="book"
a=s[:(len(s)//2)]
b=s[(len(s)//2):]
print(a)
print(b)
cheak={'a','e','i','o','u','A','E','I','O','U'}
acount=0
bcount=0
for i in range(len(a)):
    if(a[i] in cheak):
        acount+=1
    if(b[i] in cheak):
        bcount+=1
print(acount==bcount)"""
