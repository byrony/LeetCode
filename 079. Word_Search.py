class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, m, n, i, j):
                    return True
        return False
    
    def dfs(self, board, word, k, m, n, i, j):
        if len(word) == k:
            return True
        
        if i<0 or i>= m or  j<0 or j>= n or k >=len(word) or board[i][j] != word[k]:
            return False
      
        board[i][j] += '#'
        # note the short circuit, if one is True no need to evaluate others
        # d = self.dfs(board, word, k+1, m, n, i+1, j)
        # u = self.dfs(board, word, k+1, m, n, i-1, j)
        # r = self.dfs(board, word, k+1, m, n, i, j+1)
        # l = self.dfs(board, word, k+1, m, n, i, j-1)
        # res = d or u or r or l
        
        res = self.dfs(board, word, k+1, m, n, i+1, j) or self.dfs(board, word, k+1, m, n, i-1, j) \
        or self.dfs(board, word, k+1, m, n, i, j+1) or self.dfs(board, word, k+1, m, n, i, j-1)

        ## backtracking, convert board[i][j] to original value
        board[i][j] = board[i][j][0]

        return res