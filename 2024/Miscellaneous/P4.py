#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/arithmetic-slices/description/

#S O L U T I O N

from functools import cache
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i == n:
                return 0

            res = 0

            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                res += 1 + dp(i + 1)

            return res

        ans = 0

        for i in range(2, n):
            ans += dp(i)

        return ans
