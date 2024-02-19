#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2024-02-19

# 231. Power of Two



# S O L U T I O N
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1


    