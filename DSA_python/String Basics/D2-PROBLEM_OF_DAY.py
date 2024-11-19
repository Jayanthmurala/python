# Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19

"""Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions"""


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        start=0 #0 
        temp=k
        end= len(nums)-k # 3
        max=0
        while(start <= end):
            num=nums[start:temp]
            if len(set(num))!=k:
                start+=1
                temp+=1
                continue
            else:
                summ=sum(num)
                if max < summ:
                    max=summ
                temp+=1
                start+=1
        return max

s=Solution()
print(s.maximumSubarraySum(nums = [1,1,1,7,8,9], k = 3))



        