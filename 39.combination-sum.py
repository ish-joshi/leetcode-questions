#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:

    def getNext(self, csum: int, options: List[int], target: int):
        # What if there are negative numbers?
        remaining = target - csum
        return list ( filter (lambda i: i <= remaining, options))

    sols = []

    def aux(self, psol, candidates, target):

        csum = sum(psol)

        if csum == target:
            self.sols.append([i for i in psol])
        
        for option in self.getNext(csum, candidates, target):
            psol.append(option)
            self.aux(psol, candidates, target)
            psol.pop()
    

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.aux([], candidates, target)

        return self.sols
        
# @lc code=end

