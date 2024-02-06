#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06

#S O L U T I O N

# # class Solution:
# #     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# #         mp = {}
# #         ans = []

# #         for s in strs:
# #             # print("this is s:", s)
# #             # print("this is mp:",mp)
# #             # print("this is ans:",ans)
# #             sorted_str = ''.join(sorted(s))
# #             if sorted_str in mp:
# #                 ans[mp[sorted_str]].append(s)
# #             else:
# #                 mp[sorted_str] = len(ans)
# #                 ans.append([s])
                
# #         return ans

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

