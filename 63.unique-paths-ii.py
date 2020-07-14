#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # make the cols and rows 0

        rs = len(obstacleGrid)
        
        if rs == 0:
            return 0
        
        if rs == 1:
            booleans = map (lambda n : n == 1, obstacleGrid[0])
        
            # if there's 0's output 1
            # if any 1 output 0

            if any(booleans):
                return 0
            else:
                return 1

        cs = len(obstacleGrid[0])


        for r in range(rs):
            for c in range(cs):
                val = obstacleGrid[r][c]
                if val == 1:
                    obstacleGrid[r][c] = -1

        for r in range(rs):
            obstacleGrid[r][0] = 1
        
        for c in range(cs):
            obstacleGrid[0][c] = 1

        print(obstacleGrid)

        for r in range(1, rs):
            for c in range(1, cs):
                val = obstacleGrid[r][c]
                # Skip if 1 as it is an obstacle
                if val != -1:
                    top = obstacleGrid[r-1][c]
                    top = top if top != -1 else 0
                    left = obstacleGrid[r][c-1]
                    left = left if left != -1 else 0

                    obstacleGrid[r][c] = top + left

        return 0 if obstacleGrid[-1][-1] == -1 else obstacleGrid[-1][-1]

# if __name__ == "__main__":
#     Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
# @lc code=end

