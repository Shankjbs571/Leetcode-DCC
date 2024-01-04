#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/

#S O L U T I O N

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r and arr[l+1] >= arr[l]:
            l += 1
        if l == len(arr) - 1:
            return 0 # whole array is sorted
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        toRemove = min(len(arr) - l - 1, r) # case (1) and (2)
		
		# case (3): try to merge
        for iL in range(l+1):
            if arr[iL] <= arr[r]:
                toRemove = min(toRemove, r - iL - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return toRemove
    

    
    
