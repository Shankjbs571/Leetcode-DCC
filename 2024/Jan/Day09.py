#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/leaf-similar-trees/?envType=daily-question&envId=2024-01-09

#S O L U T I O N

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyparsing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafValues1=[]
        leafValues2=[]

        def traverse(node, leafValues):
            if node != None:
                if node.left == None and node.right == None:
                    leafValues.append(node.val)
                traverse(node.left, leafValues)
                traverse(node.right, leafValues)

        traverse(root1, leafValues1)
        traverse(root2, leafValues2)

        return leafValues1 == leafValues2
        


        
            
            

