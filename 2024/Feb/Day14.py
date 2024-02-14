#📚 Problem Sources:
# Leetcode: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/?envType=daily-question&envId=2024-02-14


# S O L U T I O N

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = []
#         neg = []
#         result = []
#         turn = True

#         for num in nums:
#             # print("num: ",num)
#             # print("turn: ",turn)
            


#             if turn and num>0 :
#                 if pos != []:
#                     element = pos.pop(0)
#                     result.append(element)
#                     turn = not turn
#                     pos.append(num)
#                 else:
#                     result.append(num)
#                     turn = not turn
                
#             elif turn and num<0:
#                 if pos != []:
#                     element = pos.pop(0)
#                     result.append(element)
#                     turn = not turn
#                 neg.append(num)
#             elif not turn and num<0:
#                 if neg != []:
#                     element = neg.pop(0)
#                     result.append(element)
#                     turn = not turn
#                     neg.append(num)
#                 else:
#                     result.append(num)
#                     turn = not turn
#             elif not turn and num>0:
#                 if neg != []:
#                     element = neg.pop(0)
#                     result.append(element)
#                     turn = not turn
#                 pos.append(num)
#             # print("present pos: ",pos)
#             # print("present neg: ",neg)
#             # print(result)

#         while pos != [] or neg != []:
#             if turn:
#                 element = pos.pop(0)
#                 result.append(element)
#                 turn = not turn
#             else:
#                 element = neg.pop(0)
#                 result.append(element)
#                 turn = not turn

#         return result
#         # print(result)
#         # print(neg)
#         # print(pos)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        i_pos, i_neg = 0, 1
        for num in nums:
            if num > 0:
                i = i_pos
                i_pos += 2
            else:
                i = i_neg
                i_neg += 2

            result[i] = num
        
        return result

        