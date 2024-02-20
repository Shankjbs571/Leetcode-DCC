#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/missing-number/description/?envType=daily-question&envId=2024-02-20

# 268. Missing Number



# S O L U T I O N
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
