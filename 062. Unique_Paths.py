class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic = dict()
        return self.helper(m, n, dic)
    
    # can use tuple as dictionary key
    def helper(self, m, n, dic):
        if m == 1 or n == 1:
            return 1
        
        if (m, n) in dic.keys():
            return dic[(m, n)]
        else:
            temp = self.helper(m-1, n, dic) + self.helper(m, n-1, dic)
            dic[(m, n)] = temp
            return temp
    