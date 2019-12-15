# Dec 13 2019

class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        stack = [s[0]]
        for p in s[1:]:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            elif p == ')' and stack and stack[-1] == '(':
                stack.pop()
                continue
            elif p == ']' and stack and stack[-1] == '[':
                stack.pop()
                continue
            elif p == '}' and stack and stack[-1] == '{':
                stack.pop()
                continue
            else:
                return False
        return stack == []
        