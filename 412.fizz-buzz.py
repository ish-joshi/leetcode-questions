#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:

    def fbRes(self, n):
        d3 = n%3 == 0
        d5 = n%5 == 0
        if d3 and d5:
            return "FizzBuzz"
        elif d3:
            return "Fizz"
        elif d5:
            return "Buzz"
        else:
            return str(n)

    def fizzBuzz(self, n: int) -> List[str]:
        return [self.fbRes(i+1) for i in range(n)]
        
# @lc code=end

