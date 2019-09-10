class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        ## initial a same size matrix to store max length of square at each (i,j)
        ## dp[i,j] is the lenght of square whose right bottom corner is (i,j)
        dp = [[0 for i in matrix[0]] for j in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] == '0'
        
        return (max([max(i) for i in dp]))**2