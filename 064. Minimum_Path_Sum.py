# recursion only. Time exceeded
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        return self.helper(grid, m, n)
    
    def helper(self, grid, m, n):
        """ Think it finding the path from right bottom to left top
        return: the minimal path for the sub grid from [m,n] to [0,0]
        """
        if m == 0 and n == 0:
            return grid[m][n]
        elif m > 0 and n > 0:
            return grid[m][n] + min(self.helper(grid, m-1, n), self.helper(grid, m, n-1))
        elif m == 0 and n > 0:
            return grid[m][n] + self.helper(grid, m, n-1)
        elif m > 0 and n == 0:
            return grid[m][n] + self.helper(grid, m-1, n)

# recursion with Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        path = [[-1 for i in range(n+1)] for j in range(m+1)]
        
        return self.helper(grid, m, n, path)
    
        # note: path = [[-1]*(n+1)]*(m+1) doesn't work
        # https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    
    def helper(self, grid, m, n, path):
        """ Think it finding the path from right bottom to left top.
        @path: matrix save the path sum from [m,n] to [i,j] (any index in the grid)
        return: the minimal path for the sub grid from [m,n] to [0,0]
        """
        if path[m][n] != -1:
            return path[m][n]
        
        if m == 0 and n == 0:
            path[m][n] = grid[m][n]
            return path[m][n]
        elif m == 0 and n > 0:
            path[m][n] = grid[m][n] + self.helper(grid, m, n-1, path)
            return path[m][n]
        elif m > 0 and n == 0:
            path[m][n] = grid[m][n] + self.helper(grid, m-1, n, path)
            return path[m][n]
        elif m > 0 and n > 0:
            path[m][n] = grid[m][n] + min(self.helper(grid, m-1, n, path), self.helper(grid, m, n-1, path))
            return path[m][n]