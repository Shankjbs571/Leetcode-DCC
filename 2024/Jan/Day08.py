#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/range-sum-of-bst/?envType=daily-question&envId=2024-01-08

#S O L U T I O N
from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def leafSum(node):
            if node is None:
                return

            if low <= node.val <= high:
                self.total += node.val

            if node.val > low:
                leafSum(node.left)
            
            if node.val < high:
                leafSum(node.right)
         
        leafSum(root)
        return self.total