# https://leetcode.com/problems/length-of-last-word/description/
# Input: 
# Output: 5
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
    

g= "   fly me   to   the moon  "
s=Solution()
s.lengthOfLastWord(g)
print(s.lengthOfLastWord(g))