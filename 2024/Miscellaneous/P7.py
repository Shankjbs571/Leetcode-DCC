#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/first-letter-to-appear-twice/description/

#S O L U T I O N
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char = []
        for c in s:
            if not char==[]:
                if c in char:
                    return c
                char.append(c)
            else:
                char.append(c)
            
        return ''
            




            

            
            


        
        