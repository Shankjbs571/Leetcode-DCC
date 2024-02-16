#📚 Problem Sources:
# Leetcode:https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16
# 1481. Least Number of Unique Integers after K Removals


# S O L U T I O N

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp={}

        for e in arr:
            mp[e]=mp.get(e,0)+1

        freq = list(mp.values())
        freq.sort()

        K=0
        for i in range(len(freq)):
            K+=freq[i]

            if K>k:
                return len(freq)-i

        return 0



        
        