# Jan 28 2020

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        idx = 0
        stack = [S[0]]
        for i in range(1, len(S)):
            if not stack or S[i] == stack[-1]:
                stack.append(S[i])
            elif stack[-1] == '(' and S[i] == ')':
                stack.pop()
                # if stack is empty, then reached a primitive parenthese, remove outermost parentheses and append to result
                if not stack:
                    res += S[idx+1:i]
                    idx = i+1
        return res