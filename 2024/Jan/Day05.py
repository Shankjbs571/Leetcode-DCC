#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/longest-increasing-subsequence/?envType=daily-question&envId=2024-01-05

#S O L U T I O N

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         n = len(nums)
#         dp = [1] * n

#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

# [10,9,2,5,3,7,101,18]

import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for n in nums:
            print("for n: ",n)
            insert_index = bisect.bisect_left(dp, n)
            print("inse index: ",insert_index)
            if insert_index == len(dp):
                dp.append(n)
            else:
                dp[insert_index] = n

            print("dp: ",dp)        
        return len(dp)
    
    
    
