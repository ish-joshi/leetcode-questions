#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        nl = len(nums)

        if nl == 0:
            return 0
        elif nl <= 2:
            return max(nums)
        
        memo = [0] * nl
        memo[0] = nums[0]
        memo[1] = max(nums[0:2])

        for i in range(2, nl):

            memo[i] = max (nums[i] + memo[i-2], memo[i-1])
        
        return max(memo)
        
# @lc code=end

