# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
#  Therefore only 12 and 7896 contain an even number of digits.
l=[12,345,2,6,7896]
def even(h):
    count=0
    for i in l:
        if(i>9 and evenchek(i)):
            count+=1
    return count
    
def evenchek(j):
    sum=0
    if(j>9):
        for i in str(j):
            sum+=int(i)
    return sum%2==0
print(even(l))
