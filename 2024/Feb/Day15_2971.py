#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/?envType=daily-question&envId=2024-02-15


# 2971. Find Polygon With the Largest Perimeter

# S O L U T I O N
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_elements = 0
        result = -1
        for num in nums:
            if num < sum_of_elements:
                result = num + sum_of_elements
            sum_of_elements += num
        return result