#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """Bit of an interesting question. However, this may have an easy solutions
        Looking at exploring divide and conquer approach. 
        if odd, it cannot be a power
        if even
        18 // 2, if at any point in division it's odd it's wrong
        16 // 2 => 8 // 2 => 4 // 2 => 2 // 2 => 1 and must terminate at 1
        Then the algorithm would work

        Another approach is to precompute it and store them in a set. 
        Although memory intensive, it'll deliver results faster if this function
        is used often. 

        Args:
            n (int): an integer to determine if its power of 2

        Returns:
            bool: if it is power of 2
        """

        if n == 0:
            return False
        
        elif n == 1:
            return True
        
        if n % 2 == 1:
            return False # it is an odd number
        
        while n > 1:
            if n % 2 == 1:
                return False
            n = n // 2
        
        return n == 1
            
        
# @lc code=end

