#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21


#S O L U T I O N
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, norob = 0, 0
        for num in nums:
            newRob = norob + num
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
        return max(rob, norob)