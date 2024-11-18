# https://leetcode.com/problems/reverse-string/
# reverse-string

s1 = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """s.reverse()
        print(s)"""
        # OR
        """print(s[::-1])"""
        # OR
        start_index=0
        end_index=len(s)-1
        while(start_index < end_index):
            TEMP=s[start_index]
            s[start_index]=s[end_index]
            s[end_index]=TEMP
            start_index+=1
            end_index-=1
        print(s)
        
solution=Solution()
solution.reverseString(s)