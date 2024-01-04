#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/?envType=daily-question&envId=2024-01-04

#S O L U T I O N

from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1: 
                return -1
            ans += ceil(c / 3)
        return ans
    
# sol=Solution()
# list=[2,3,3,2,2,4,2,3,4]
# print(sol.minOperations(list))
    
    