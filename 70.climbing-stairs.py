#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:

    cache = {i:i for i in range(0,4)}

    def fib(self, n):
        """Memoized fibonacci. Could do using loop but wanted to try this one out

        Args:
            n (int): fib till n

        Returns:
            int: fibonacci till n
        """
        if n in range(0,4):
            return n
        
        if self.cache.get(n-1) is None:
            self.cache[n-1] = self.fib(n-1)
        if self.cache.get(n-2) is None:
            self.cache[n-1] = self.fib(n-1)

        nm1 = self.cache.get(n-1)
        nm2 = self.cache.get(n-2)

        return nm1 + nm2


    def climbStairs(self, n: int) -> int:
        return self.fib(n)
# @lc code=end

