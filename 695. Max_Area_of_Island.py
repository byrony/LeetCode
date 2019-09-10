# iterative
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])        
        
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = self.dfs(grid, i, j, m, n)
                    area = max(temp, area)
        return area
        
    def dfs(self, grid, i, j, m, n):
        area = 0
        land = [(i,j)]
        while land:
            i, j = land.pop()
            if grid[i][j] == 1:
                area += 1
                grid[i][j] = -1

            if j < n-1 and grid[i][j+1] == 1:
                land.append((i, j+1))
            if i < m-1 and grid[i+1][j] == 1:
                land.append((i+1, j))
            if j > 0 and grid[i][j-1] == 1:
                land.append((i, j-1))
            if i > 0 and grid[i-1][j] == 1:
                land.append((i-1, j))
        return area


## recursive
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])        
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, m, n)
                    maxArea = max(area, maxArea)
        return maxArea
        
    def dfs(self, grid, i, j, m, n):
        if 0<=i<m and 0<=j<n and grid[i][j]==1:
            grid[i][j] = -1
            return 1 + self.dfs(grid, i, j+1, m, n) + self.dfs(grid, i+1, j, m, n) + self.dfs(grid, i, j-1, m, n) + self.dfs(grid, i-1, j, m, n)
        
        else:
            return 0