#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List
class Solution:
    """Learnings; check for empty or 1 element case for edge cases.
    2D grids can be tricky to traverse and comprehend due to references and issues caused by it. 
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        """The function attempts to find the best path from top left to bottom right; move only right and down.

        Args:
            grid (List[List[int]]): 2D Grid

        Returns:
            int: The minimum weight of the path that is possible.
        """

        if len(grid) == 0:
            return 0
        elif len(grid) == 1:
            return sum(grid[0])

        # The first row and first column will be the sum basically.
        for r in range(1, len(grid)):
            # set column 0 of each row to sum
            grid[r][0] = grid[r-1][0] + grid[r][0]
        
        for c in range(1, len(grid[r])):
            # set each row first to sum
            grid[0][c] = grid[0][c-1] + grid[0][c]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                value = grid[r][c]
                grid[r][c] = min (value + grid[r-1][c], value + grid[r][c-1])
 
        return grid[-1][-1]

# if __name__ == "__main__":
#     print (Solution().minPathSum([[1,2,3],[4,5,6]]))
# @lc code=end

