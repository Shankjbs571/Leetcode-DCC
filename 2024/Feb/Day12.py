#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/majority-element/description/?envType=daily-question&envId=2024-02-12


# S O L U T I O N
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         required_freq = len(nums)//2
#         mp={}
#         for num in nums:
#             mp[num]=mp.get(num,0)+1
#         # print(mp)

#         for num in mp:
#             if mp[num]>required_freq:
#                 return num

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate