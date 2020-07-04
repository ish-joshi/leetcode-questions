#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 0:
            return False
        newBed = [0]  + flowerbed + [0]
        placed = 0
        for i in range(1, len(flowerbed) + 1):
            prev, mid, af = newBed[i-1:i+2]
            if mid == 1:
                continue
            elif prev == 0 and af == 0:
                newBed[i] = 1
                placed += 1
        
        return placed >= n

        
# @lc code=end

