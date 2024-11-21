# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are . On reversing the vowels, s becomes "AceCreIm".


# Input: s = "leetcode"

# Output: "leotcede"

s = "IceCreAm" 
class Solution:
    def reverseVowels(self, s: str) -> str:
        v= set('aeiouAEIOU')
        l=list(s)
        left =0
        right = len(s)-1

        while( left < right):
            if l[left] not in v:
                left +=1
            elif l[right] not in v:
                right -=1
            else:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
                
        return ''.join(l)

s="leetcode"
print()
S=Solution()
print(S.reverseVowels(s))
