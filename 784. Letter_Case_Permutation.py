# Sep 15, 2019
# DFS Method
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        length = len(S)
        res = []
        self.dfs(S, '', res, length)
        return res
    
    def dfs(self, S, arr, res, length):
        if len(arr) < length:
            for i, c in enumerate(S):
                if c.isalpha():
                    self.dfs(S[i+1:], arr+c.lower(), res, length)
                    self.dfs(S[i+1:], arr+c.upper(), res, length)
                elif c.isdigit():
                    self.dfs(S[i+1:], arr+c, res, length)
        elif len(arr) == length:
            res.append(arr)
        else:
            return
        

## Sep 15, 2019
# BFS Method. Much faster than DFS
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = self.bfs(S, [''])
        return res
    
    def bfs(self, S, res):
        for i, c in enumerate(S):
            tmp = []
            for r in res:
                if c.isalpha():
                    tmp.append(r+c.upper())
                    tmp.append(r+c.lower())
                elif c.isdigit():
                    tmp.append(r+c)
            res = tmp
        return res