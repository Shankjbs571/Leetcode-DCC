#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

#S O L U T I O N
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         prev=nums[0]
#         prevcount=0
#         ans=[]
#         for i in range(1,len(nums)):
#             if nums[i]==prev:
#                 if i==len(nums):
#                     ans.append(nums[i]-1)
#                     ans.append(nums[i])
#                     return ans
#                 else:
#                     ans.append(nums[i]-1)
#                     ans.append(nums[i])
#                     return ans

#             else:
#                 prev=nums[i]
                
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)//2-sum(set(nums))]
        

