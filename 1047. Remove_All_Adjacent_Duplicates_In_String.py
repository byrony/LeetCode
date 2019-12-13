# Dec 11 2019

class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        i = 0
        j = 1
        while j < len(S):
            if S[i] != S[j]:
                i += 1
                j += 1
            else:
                S = S[0:i]+S[j+1:]
                i = max(0, i-1)
                j = max(1, j-1)
        return S


# using stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]
        for s in S[1:]:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
