# Dec 15 2019

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = int(len(arr)/4)+1
        stack = []
        for a in arr:
            if not stack:
                stack.append(a)
                if len(stack) >= cnt:
                    return a
            elif a == stack[-1]:
                stack.append(a)
                if len(stack) >= cnt:
                    return a
            elif a != stack[-1]:
                stack = [a]
            
        