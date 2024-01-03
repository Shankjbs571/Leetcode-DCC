#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/set-matrix-zeroes/description/


#S O L U T I O N


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        """Loop through matrix and track rows and cols with zeros"""
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        """Loop through matrix again"""
        """Set zeros if row / col in sets from above"""
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in rows or c in cols:
                    matrix[r][c] = 0