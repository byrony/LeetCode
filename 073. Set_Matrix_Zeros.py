class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = 0
        row_zero = set()
        col_zero = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zero.update({i})
                    col_zero.update({j})
        
        ## update rows with zero
        for t in row_zero:
            matrix[t][0:n] = [0 for i in range(n)]
        
        ## update cols with zero
        for i in range(m):
            for c in col_zero:
                #print(i, c)
                matrix[i][c] = 0


## constant space solution. Use two Boolean variable to store whether 1st row and 1st col contains 0.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row_1st_0 = False
        col_1st_0 = False
        
        ## check whether 1st row and 1st col contains 0
        for i in range(n):
            if matrix[0][i] == 0:
                row_1st_0 = True
                break
        for j in range(m):
            if matrix[j][0] == 0:
                col_1st_0 = True
                break
        
        ## check row 1:m and col 1:n, store the 0 indicator to 1st row and 1st col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        ## update cols to zero except 1st row
        for i in range(1, n):
            if matrix[0][i] == 0:
                for r in range(1, m):
                    matrix[r][i] = 0
        
        ## update rows to zero except 1st col
        for j in range(1, m):
            if matrix[j][0] == 0:
                matrix[j][1:n] = [0 for i in range(n-1)]
                
        ## update 1st row and 1st col to 0
        if row_1st_0:
            matrix[0][0:n] = [0 for i in range(n)]
        if col_1st_0:
            for r in range(m):
                matrix[r][0] = 0
                
        

                
        