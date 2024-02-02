#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/sequential-digits/submissions/1163758337/?envType=daily-question&envId=2024-02-02

#S O L U T I O N
# class Solution:
#     def sequentialDigits(self, low, high):
#         a = []

#         for i in range(1, 10):
#             num = i
#             next_digit = i + 1

#             while num <= high and next_digit <= 9:
#                 num = num * 10 + next_digit
#                 if low <= num <= high:
#                     a.append(num)
#                 next_digit += 1

#         a.sort()
#         return a

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = '123456789'
        l = []
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                if low <= int(t[i:j]) <= high:
                    l.append(int(t[i:j]))
        return sorted(l)
        