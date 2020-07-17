#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
class Solution:

    res = []

    def getNext(self, partial, nums):
        return list (set(nums) -  set(partial))

    def aux(self, partial, nums):
        self.res.append([i for i in partial]) # Python has references

        for opt in self.getNext(partial, nums):
            partial.append(opt)
            self.aux(partial, nums)
            partial.pop()
        
        print(partial, nums)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.aux([], nums)
        return self.res


# if __name__ == "__main__":
#     s = Solution()
#     r = s.subsets([1,2,3])
#     print(r)
# @lc code=end

