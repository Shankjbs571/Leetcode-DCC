#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/minimum-falling-path-sum/description/?envType=daily-question&envId=2024-01-19

#S O L U T I O N

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev = matrix[0]
        for i in range(1, m):
            curr = [maxsize] * n
            for j in range(n):
                if j == 0:
                    curr[j] = matrix[i][j] + min(prev[j], prev[j+1])
                elif j == n-1:
                    curr[j] = matrix[i][j] + min(prev[j], prev[j-1])
                else:
                    curr[j] = matrix[i][j] + min(prev[j-1], prev[j], prev[j+1])
            prev = [i for i in curr]
        return min(prev)