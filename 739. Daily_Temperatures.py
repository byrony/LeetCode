# Jan 4 2020

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        for i in range(len(T)-1, -1, -1):
            
            while stack:
                nextday, idx = stack[-1]
                if nextday <= T[i]:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = idx - i
        
            stack.append((T[i], i))
            # print(stack)
        return res