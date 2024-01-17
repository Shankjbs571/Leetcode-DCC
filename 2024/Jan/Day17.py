#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=daily-question&envId=2024-01-17


#S O L U T I O N

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         arr.sort()
#         v = []

#         i = 0
#         while i < len(arr):
#             cnt = 1

#             # Count occurrences of the current element
#             while i + 1 < len(arr) and arr[i] == arr[i + 1]:
#                 cnt += 1
#                 i += 1

#             v.append(cnt)
#             i += 1

#         v.sort()

#         for i in range(1, len(v)):
#             if v[i] == v[i - 1]:
#                 return False

#         return True

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values()))==len(Counter(arr).values())
        