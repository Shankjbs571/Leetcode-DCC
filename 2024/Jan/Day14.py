#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14

#S O L U T I O N

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         freq1 = [0] * 26
#         freq2 = [0] * 26

#         for ch in word1:
#             freq1[ord(ch) - ord('a')] += 1

#         for ch in word2:
#             freq2[ord(ch) - ord('a')] += 1

#         for i in range(26):
#             if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
#                 return False

#         freq1.sort()
#         freq2.sort()

#         for i in range(26):
#             if freq1[i] != freq2[i]:
#                 return False

#         return True
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = len(word1)
        l2 = len(word2)
        if l1 != l2: return False
        w1 = set(word1)
        if w1 != set(word2): return False
        wd1 = []
        wd2 = []
        for i in w1:
            wd1.append(word1.count(i))
            wd2.append(word2.count(i))
            
        if sorted(wd1) != sorted(wd2): return False
        

        return True

    