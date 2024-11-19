# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/


# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.find(needle)
    
s=Solution()
print(s.strStr(haystack = "butsad", needle = "sad"))
