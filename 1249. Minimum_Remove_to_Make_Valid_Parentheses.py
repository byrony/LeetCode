# Jan 29 2019

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par = []
        for i, n in enumerate(s):
            if n == '(':
                par.append((n, i))
            elif n == ')' and len(par)>=1 and par[-1][0] == '(':
                par.pop()
            elif n == ')':
                par.append((n, i))
                
        remove_idx = set([i for n, i in par])
        return ''.join([s[j] for j in range(len(s)) if j not in remove_idx])