#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=daily-question&envId=2024-02-05

#S O L U T I O N


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}

        for a in s: 
            mp[a] = mp.get(a, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1




            

            
            


        