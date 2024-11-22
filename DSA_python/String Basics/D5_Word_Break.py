# https://leetcode.com/problems/word-break/description/


# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
# space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
# Input: , 
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.




s = "leetcode"
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)  # Use a set for faster lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Stop further checks for this i
        
        return dp[n]

    
wordDict = ["leet","code"]
S= Solution()
print(S.wordBreak(s,wordDict))

