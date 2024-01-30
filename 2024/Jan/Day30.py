#📚 Problem Sources:
# Leetcode:
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

#S O L U T I O N

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) >= 2:
            relist=[]
            for o in tokens:
                if o in ['+', '-', '*', '/']:
                    x = int(relist.pop(-2))
                    y = int(relist.pop(-1))
                    match o:
                        case '+':
                            result = x + y
                            relist.append(result)
                        case '-':
                            result = x - y
                            relist.append(result)
                        case '*':
                            result = x * y
                            relist.append(result)
                        case '/':
                            result = x / y
                            relist.append(result)
                else:
                    relist.append(o)

            # print(relist)
            return int(relist[0])
        else:
            return int(tokens[0])
                    
                        