#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/submissions/1162940987/?envType=daily-question&envId=2024-02-01

#S O L U T I O N

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
        return ans