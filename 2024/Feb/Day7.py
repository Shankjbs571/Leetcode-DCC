#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=daily-question&envId=2024-02-07

# S O L U T I O N

class Solution:
    def frequencySort(self, s: str) -> str:
        count_mp={}
        
        for c in s:
            count_mp[c] = count_mp.get(c,0)+1

        my_list = list(count_mp.items())
        # Sort the list based on the second element of each tuple
        sorted_list = sorted(my_list, key=lambda x: x[1],reverse=True)

        # # Print the sorted list
        # print(sorted_list)

        ans=''
        for t in sorted_list:
            ans+=t[1]*t[0]
        return ans
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # Step 1: Count the frequency of each character
#         char_count = Counter(s)
        
#         # Step 2: Sort characters based on their frequency in descending order
#         sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

#         # Step 3: Build the result string by repeating characters according to their frequency
#         result = ''
#         for char in sorted_chars:
#             result += char * char_count[char]
        
#         # Step 4: Return the final sorted string
#         return result