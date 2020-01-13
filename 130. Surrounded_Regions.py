# Jan 9 2020

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_visit = set()
        bad_region = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in all_visit or board[i][j] != 'O':
                    continue
                elif board[i][j] == 'O':
                    region = []
                    good = [True]
                    visit = set()
                    self.bfs(board, i, j, visit, region, good)
                    if not good[0]:
                        bad_region += region
                    all_visit.update(visit)
        
        # change bad_region back to 'O'
        for i, j in bad_region:
            board[i][j] = 'O'
        return
        
    def bfs(self, board, i, j, visit, region, good):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if board[i][j] != 'O':
            return
        else:
            board[i][j] = 'X'
            visit.add((i,j))
            region.append((i,j))
            if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                good[0] = False
        
            if i>0:
                self.bfs(board, i-1, j, visit, region, good)
            if i<len(board)-1:
                self.bfs(board, i+1, j, visit, region, good)
            if j>0:
                self.bfs(board, i, j-1, visit, region, good)
            if j<len(board[0])-1:
                self.bfs(board, i, j+1, visit, region, good)
        