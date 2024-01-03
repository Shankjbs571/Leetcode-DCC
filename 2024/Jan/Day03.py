#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2024-01-03

#S O L U T I O N

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_sum=0
        total_lines=0
        for s in bank:
            digits = [int(digit) for digit in s]
            d_sum = sum(digits)
            if d_sum!=0 and prev_sum==0:
                prev_sum=d_sum
            elif d_sum!=0 and prev_sum!=0:
                lines=prev_sum*d_sum
                total_lines+=lines
                prev_sum=d_sum

        return total_lines