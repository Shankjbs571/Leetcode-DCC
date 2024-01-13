#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

#S O L U T I O N

class Solution:
    def minSteps(self, s, t):
        count = [0] * 26
        # Storing the difference of frequencies of characters in t and s.
        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1

        ans = 0
        # Adding the difference where string t has more instances than s.
        # Ignoring where t has fewer instances as they are redundant and
        # can be covered by the first case.
        for i in range(26):
            ans += max(0, count[i])

        return ans
