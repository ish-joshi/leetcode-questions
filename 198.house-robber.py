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
        
        
        a = nums[0]
        b = max(nums[0:2])
        mv = max(a, b)
        
        # This only needs previous two values. The whole memo array is not needed. 
        # Optimize by storing as a, b where a = memo[i-2], b = memo[i-1]
        # Res can just be max at all times. :) 

        for i in range(2, nl):

            c = max (nums[i] + a, b)
            a = b
            b = c

            mv = max(mv, c)
        
        return mv
        
# @lc code=end

