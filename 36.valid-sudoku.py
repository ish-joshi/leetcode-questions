#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:

    def getCol(self, colId, board):
        col = [i for i in range(9)]
        return list ( map (lambda row: board[row][colId], col))

    def getRow(self, rowId, board):
        return board[rowId]
    
    def nonRepeatingNumbers(self, items):
        filtered = list ( filter(lambda item: item != ".", items))
        return len(filtered) == len(set(filtered))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            irow = self.getRow(i, board)
            icol = self.getCol(i, board)

            if not self.nonRepeatingNumbers(irow):
                return False
            elif not self.nonRepeatingNumbers(icol):
                return False
        
        # All rows and cols have been checked
        return True
        
# @lc code=end

