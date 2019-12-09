# Dec 8 2019

# Bottom-up
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        DP:  
        numTrees(0 to n) = for i in 0,1,2,3,...,n, sum of 
        numTrees(0 to i-1)*numTrees(i+1 to n), where numTrees(i+1 to n)
        equals to numTrees(0 to n-i-1)
        '''
        dic  = dict()
        dic[0] = 1
        dic[1] = 1
        dic[2] = 2
        for i in range(3, n+1):
            temp = 0
            for j in range(0, i):
                temp += dic[j]*dic[i-j-1]
            dic[i] = temp
        return dic[n]


# top down
class Solution:
    def numTrees(self, n: int) -> int:
        dic  = dict()
        dic[0] = 1
        dic[1] = 1
        dic[2] = 2
        return self.dp(n, dic)
        
    def dp(self, n, dic):
        if n in dic.keys():
            return dic[n]
        temp = 0
        for i in range(0, n):
            temp += self.dp(i, dic) * self.dp(n-i-1, dic)
        dic[n] = temp
        return dic[n]