#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start

from functools import reduce

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        lc = len (list(filter (lambda c: ord('a') <= ord(c) <= ord('z'), word)))
        uc = len(word) - lc

        allLc = lc == len(word)
        allUc = uc == len(word)

        if any([allLc, allUc]):
            return True
        
        return uc == 1 and ( ord('A') <= ord(word[0]) <= ord('Z'))


        
# @lc code=end

