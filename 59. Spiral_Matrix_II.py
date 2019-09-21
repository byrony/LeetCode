class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for j in range(n)]

        c1, c2 = 0, len(matrix)-1
        r1, r2 = 0, len(matrix[0])-1
        
        value = 1
        while c1<=c2 and r1<=r2:
            if c1 == c2 and r1 == r2:
                matrix[r1][c1] = value
                break
                
            for c in range(c1, c2):
                matrix[r1][c] = value
                value += 1
            for r in range(r1, r2):
                matrix[r][c2] = value
                value += 1
            for c in range(c2, c1, -1):
                matrix[r2][c] = value
                value += 1
            for r in range(r2, r1, -1):
                matrix[r][c1] = value
                value += 1
            c1 += 1
            c2 -= 1
            r1 += 1
            r2 -= 1

        return matrix