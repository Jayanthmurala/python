# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

# 1876. Substrings of Size Three with Distinct Characters



class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l_s=len(s)
        op=[]
        for i in range(l_s):
            for j in range(i,l_s):
                temp=''
                for k in range(i,j+1):
                    temp = temp + s[k]
                if len(temp)==3:
                    op.append(temp)
                        
        res=list(map(set,op))
        ans=list(filter(lambda x : len(x)==3,res))
        return len(ans)
    



Word = "aababcabc"
S=Solution()
print(S.countGoodSubstrings(Word))