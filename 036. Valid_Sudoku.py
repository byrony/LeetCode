class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            board[i] = list(board[i])

        # check each row
        for each_line in board:
            dic = {}
            for each_elemt in each_line:
                if each_elemt not in dic:
                    dic[each_elemt] = 1
                elif each_elemt in dic and each_elemt == '.':
                    dic[each_elemt] += 1
                else:
                    return False

        # check each column
        for i in range(len(board)):
            dic = {}
            for j in range(9):
                each_elemt = board[j][i]
                if each_elemt not in dic:
                    dic[each_elemt] = 1
                elif each_elemt in dic and each_elemt == '.':
                    dic[each_elemt] += 1
                else:
                    return False

        # check each of 9-sub boxes
        for i in range(9):
            dic = {}
            for j in range(9):
                each_elemt =  board[i//3*3 + j//3][i%3*3 + j%3]
                if each_elemt not in dic:
                    dic[each_elemt] = 1
                elif each_elemt in dic and each_elemt == '.':
                    dic[each_elemt] += 1
                else:
                    return False

        return True


