#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        if len(coins) == 0:
            return -1
        
        if len(coins) == 1:
            return (amount//coins[0]) if amount % coins[0] == 0 else -1

        coins.sort()
        remain = amount
        used = 0
        while remain > 0:
            # reduce it if it is possible

            if not coins:
                return -1

            last_amount = coins[-1]
            if last_amount > remain:
                coins.pop()
            else:
                remain -= last_amount
                used += 1
        
        print(coins, remain, used)
        return used if  remain == 0 else -1

# if __name__ == "__main__":
#     print( Solution().coinChange([2,5], 10))
    # Thinking of it as a problem that can be solved using a greedy ish approach.
# @lc code=end

