# https://leetcode.com/problems/valid-palindrome/


# Input: 
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        return filtered == filtered[::-1]
        

    # or


s = "A man, a plan, a canal: Panama"
p=s.replace(" ",'')
if "," in p:
    p=p.replace(",","")
if ":"in p:
    p=p.replace(":","")


print(p.lower()==p.lower()[::-1])