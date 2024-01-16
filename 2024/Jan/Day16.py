#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=daily-question&envId=2024-01-16

#S O L U T I O N 1

# import random
# class RandomizedSet:

#     def __init__(self):
#         self.set = set()
        

#     def insert(self, val: int) -> bool:
#         if val in self.set:
#             return False
#         else:
#             self.set.add(val)
#             return True

#     def remove(self, val: int) -> bool:
#         if val in self.set:
#             self.set.remove(val)
#             return True
#         else:
#             return False

#     def getRandom(self) -> int:
#         return random.choice(tuple(self.set))

        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()


#S O L U T I O N 2

class RandomizedSet:

    def __init__(self):
        self.dic_direct = {}
        self.dic_invert = {}
        self.num_elem = 0
        
    def insert(self, val: int) -> bool:
        if val in self.dic_invert:
            return False
        else:
            self.dic_invert[val] = self.num_elem
            self.dic_direct[self.num_elem] = val
            self.num_elem += 1
            return True
        
    def remove(self, val):
        if val not in self.dic_invert:
            return False
        else:
            ind = self.dic_invert.pop(val)
            self.dic_direct.pop(ind)
            if ind != self.num_elem - 1:
                self.dic_direct[ind] = self.dic_direct[self.num_elem - 1]
                self.dic_invert[self.dic_direct[self.num_elem - 1]] = ind
                self.dic_direct.pop(self.num_elem - 1)
            self.num_elem -= 1
            return True
        
    def getRandom(self):
        index = floor(random.random()*self.num_elem)
        return self.dic_direct[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()