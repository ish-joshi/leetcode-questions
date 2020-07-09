#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    """The solution is based on dynamic programming. 
    It fills the first row with 1's as there's only 1 possible way to get to each point (go right)
    It also fills the first column with 1's as only 1 way to go down. 
    The for each block it's a combination of just how many ways to get there (top + left)
    Pick the last grid and the result should be there! It's done.
    """

    def create2DGrid(self, rows, cols):
        return [ [0 for _ in range(cols)] for _ in range(rows) ]
    
    def prettyPrint(self, grid):
        for _ in range(len(grid)):
            print (grid[_])

    def uniquePaths(self, m: int, n: int) -> int:
        # m is number of columns
        # n is number of rows
        grid = self.create2DGrid(n, m)
        for r in range(n):
            grid[r][0] = 1
        for c in range(m):
            grid[0][c] = 1
        
        for r in range (1, n):
            for c in range(1, m):

                top = grid[r-1][c]
                left = grid[r][c-1]

                grid[r][c] = top + left
        
        # self.prettyPrint(grid)
        return grid[-1][-1]

if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))
# @lc code=end

