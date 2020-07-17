#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
## TODO: complete this
class Solution:

    LAND = 1
    WATER = 0

    def getElement(self, grid, i, j):
        if not ((0 <= i <= len(grid)) and (0 <= j <= len(grid))):
            return self.WATER
        else:
            return grid[i][j]

    def dfs(self,grid, i, j):
        if grid[i][j] == self.WATER:
            return 0
        
        

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == self.LAND:
                    self.dfs(grid, i, j)

        
# @lc code=end

