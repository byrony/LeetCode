# Dec 15 2019

# this method need be optimized
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # note in this problem, diagonal are all 1
        N = len(M)
        circleNum = 0
        seen = set()
        for i in range(N):
            if M[i][i] == 1 and i not in seen:
                circleNum += 1
                self.dfs(M, i, i, N, seen)
                seen.add(i) # ith row and ith column are clear
        return circleNum
    
    def dfs(self, M, i, j, N, seen):
        if M[i][j] == 1:
            M[i][j] = -1 
        else:
            return
    
        for t in range(0, N):
            if t not in seen:
                self.dfs(M, t, j, N, seen)
                self.dfs(M, i, t, N, seen)
        
