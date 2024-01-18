#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18

#S O L U T I O N

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        
        dp = [0] * (n + 1)
        
        dp[1] = 1  
        dp[2] = 2  
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  
        
        return dp[n] 