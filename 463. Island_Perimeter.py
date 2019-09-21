class Solution:
    def islandPerimeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        if not grid:
            return 0
        
        idx = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, m, n, idx)
                    break
        # print(idx)
    
        preimeter = 0
        for i, v in idx.items():
            for j in v:
                right, left, down, up  = 0, 0, 0, 0
                if j == n-1:
                    right = 0
                elif j+1 in v:
                    right = 1
                    
                if j == 0:
                    left = 0
                elif j - 1 in v:
                    left = 1
                    
                if i == m-1:
                    down = 0
                elif i+1 in idx.keys() and j in idx[i+1]:
                    down = 1
                    
                if i == 0:
                    up = 0
                elif i-1 in idx.keys() and j in idx[i-1]:
                    up = 1
                # print(i,j, 4-(right+left+down+up), '|', right, left, down, up)
                preimeter += 4-(right+left+down+up)
        return preimeter
    
    def dfs(self, grid, i, j, m, n, idx):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
            return
        grid[i][j] = -1
        
        if i not in idx.keys():
            idx[i] = {j}
        else:
            idx[i].update(set([j]))
        self.dfs(grid, i-1, j, m, n, idx)
        self.dfs(grid, i+1, j, m, n, idx)
        self.dfs(grid, i, j+1, m, n, idx)
        self.dfs(grid, i, j-1, m, n, idx)



class Solution:
    def islandPerimeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        if not grid:
            return 0
        
        peri_tot = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    peri_tot += self.peri_adjacent(grid, i, j, m, n)
        return peri_tot
                    
    def peri_adjacent(self, grid, i, j, m, n):
        adjacent = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        
        peri = 0
        for x, y in adjacent:
            if x<0 or x>m-1 or y<0 or y>n-1 or grid[x][y]==0:
                peri += 1
            print(i, j, peri)
        return peri