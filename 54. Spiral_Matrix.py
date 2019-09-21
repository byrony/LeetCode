class Solution:
    def spiralOrder(self, matrix):
        
        res = []
        while len(matrix)>0 and len(matrix[0])>0:
            top, right, bottom, left = [],[],[],[]

            if matrix and matrix[0]:
                top = matrix[0]
                del matrix[0]
            
            if matrix and matrix[0]:
                right = []
                for row in matrix:
                    right.append(row[-1])
                    del row[-1]

            if matrix and matrix[0]:
                bottom = matrix[-1][::-1]
                del matrix[-1]

            if matrix and matrix[0]:
                left = []
                for row in matrix:
                    left.append(row[0])
                    del row[0]
                left = left[::-1]

            res += top
            res += right
            res += bottom
            res += left
            # print(res)
        return res