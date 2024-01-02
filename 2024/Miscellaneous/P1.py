#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/find-a-peak-element-ii/description/

#S O L U T I O N

class Solution:
    def maxEl(self, mat, n, m, col):
        maxi = -1
        ind = -1
        for i in range(n):
            if mat[i][col] > maxi:
                maxi = mat[i][col]
                ind = i
        return ind

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2
            row = self.maxEl(mat, n, m, mid)
            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]