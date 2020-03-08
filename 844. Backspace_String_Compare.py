# Feb 2 2020

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for s in S:
            if s != '#':
                stack_s.append(s)
            elif s == '#' and stack_s:
                stack_s.pop()
        for t in T:
            if t != '#':
                stack_t.append(t)
            elif t == '#' and stack_t:
                stack_t.pop()
                
        return stack_s == stack_t