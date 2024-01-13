#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12

#S O L U T I O N

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        half = len(s) // 2
        a = s[0:half]
        b = s[half:len(s)]
        count = 0
        c = 0
        for i in a:
            if i in 'aeiouAEIOU':
                count+=1
        for j in b:
            if j in 'aeiouAEIOU':
                c+=1
        if c == count:
            return True
        else:
            return False