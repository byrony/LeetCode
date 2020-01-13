# Jan 11 2020

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(res, [], s)
        return res
    
    def dfs(self, res, path, s):
        if len(s) == 0:
            res.append(path)
        for i in range(len(s)):
            if self.isPal(s[:i+1]):
                self.dfs(res, path+[s[:i+1]], s[i+1:])
        
    def isPal(self, s):
        return s == s[::-1]