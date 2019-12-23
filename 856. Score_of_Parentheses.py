# Dec 20 2019

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [S[0]]
        for s in S[1:]:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append('1')
                elif stack[-1].isdigit():
                    # compute the sum of consecutive numbers
                    temp = 0
                    while stack and stack[-1].isdigit():
                        temp += int(stack.pop())
                    
                    stack.pop() # pop the "(" before the number
                    stack.append(str(temp*2))
        return sum([int(i) for i in stack])