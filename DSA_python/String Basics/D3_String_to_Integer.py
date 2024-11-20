# # https://leetcode.com/problems/string-to-integer-atoi/description/
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

"""The algorithm for myAtoi(string s) is as follows:
Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
Step 2: "42" (no characters read because there is neither a '-' nor '+')
Step 3: "42" ("42" is read in)

"""


ss=" -abc" #abc123" or " -abc"
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if s =="" or s=='-' or s=='+':
            return 0
        if len(s)>=2:
            if s[0] in ['+','-'] and s[1] in ['+','-']:
                return 0
        num='0'
        if s[0]=='-'or s[0]=='+':
            if s[0]=='-':
                num='-0'
            for i in range(1,len(s)):
                if (s[i].isdigit()):
                    num+=s[i]
                else:
                    break
        else:
            for i in range(0,len(s)):
                if (s[i].isdigit()):
                    num+=s[i]
                else:
                    break 
        if int(num) < INT_MIN:
            return INT_MIN
        if int(num) > INT_MAX:
            return INT_MAX
        
        return int(num)

s=Solution()
print(s.myAtoi(ss))
