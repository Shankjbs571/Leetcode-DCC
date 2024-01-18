#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/min-cost-climbing-stairs/description/


#S O L U T I O N
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = prev_prev = 0
        for c in cost:
            prev, prev_prev = min(prev, prev_prev)+c, prev
        return min(prev, prev_prev)