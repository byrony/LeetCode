# recursive dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j, m, n)
        # print(grid)
        return island
        
    def dfs(self, grid, i, j, m, n):
        if grid[i][j] == '1':
            land = [(i,j)]
            while land:
                i, j = land.pop()
                grid[i][j] = '#'
                
                if j < n-1 and grid[i][j+1] == '1':
                    land.append((i, j+1))
                if i < m-1 and grid[i+1][j] == '1':
                    land.append((i+1, j))
                if j > 0 and grid[i][j-1] == '1':
                    land.append((i, j-1))
                if i > 0 and grid[i-1][j] == '1':
                    land.append((i-1, j))
            
        
# iterative dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j, m, n)
        # print(grid)
        return island
            
    def dfs(self, grid, i, j, m, n):
        if grid[i][j] == '1':
            grid[i][j] = '#'
        else:
            return
        if j < n-1 and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1, m, n)
        if i < m-1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j, m, n)
        if j > 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1, m, n)
        if i > 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j, m, n)