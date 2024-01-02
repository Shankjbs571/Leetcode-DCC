#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/?envType=daily-question&envId=2024-01-02


#S O L U T I O N

class Solution:
    def findMatrix(self, nums):
        freq = [0] * (len(nums) + 1)

        ans = []
        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans