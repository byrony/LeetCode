
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dic = dict()
        return self.helper(m, n, dic, obstacleGrid)
            
    # can use tuple as dictionary key
    def helper(self, m, n, dic, obstacleGrid):
        #print(dic)
        if m == 0 or n == 0: ## this is the stopping criteria as m and n decreasing in recursion
            return 0
        elif obstacleGrid[len(obstacleGrid) - n][len(obstacleGrid[0]) - m] == 1:
            dic[(m, n)] = 0
            return 0
        elif m == 1 and n == 1: ## this condition is after previous one, then [[1]] returns 0 first
            dic[(m, n)] = 1
            return 1
        elif (m, n) in dic.keys():
            return dic[(m, n)]
        else:
            temp = self.helper(m-1, n, dic, obstacleGrid) + self.helper(m, n-1, dic, obstacleGrid)
            dic[(m, n)] = temp
            return temp



## wrong answer without inaccurate idea
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        ### check the index of obstacle
        # note that each row and each column only keeps the 1st 1. The 1st 1 contains paths of the rest 1.
        obs_idx = []
        i = 0
        j = 0
        j_rightEdge = m
          
        while i <= n-1:
            while j < j_rightEdge:
                if obstacleGrid[i][j] == 1:
                    obs_idx.append((m-j, n-i))
                    break
                else:
                    j += 1
            i += 1
            j_rightEdge = j
            j = 0
        print(obs_idx)
        
        ### special case
        if (m == 1 or n ==1) and len(obs_idx)==0:
            return 1
        elif (m==1 or n==1) and len(obs_idx)>0:
            return 0      
        
        ### dictionary to store # of paths at each index
        dic = dict()
        dic[(1,1)] = 1 # deal with dic[(m-m_+1, n-n_+1)]
        total_path = self.helper(m, n, dic)
        print(dic)
        
        obs_path = 0
        for m_, n_ in obs_idx:
            # path contains obstacle = path after * path before
            obs_path += dic[(m_, n_)] * dic[(m-m_+1, n-n_+1)]
        
        #print(total_path, obs_path)
        return total_path - obs_path
            
    # can use tuple as dictionary key
    def helper(self, m, n, dic):
        if m == 1 or n == 1:
            dic[(m, n)] = 1
            return 1
        if (m, n) in dic.keys():
            return dic[(m, n)]
        else:
            temp = self.helper(m-1, n, dic) + self.helper(m, n-1, dic)
            dic[(m, n)] = temp
            return temp