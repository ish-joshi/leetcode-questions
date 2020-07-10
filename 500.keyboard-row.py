#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row1 = {c:1 for c in list("qwertyuiop")}
        row2 = {c:2 for c in list("asdfghjkl")}
        row3 = {c:3 for c in list("zxcvbnm")}

        combined = {**row1, **row2, **row3}
        # print(combined)

        def isOneRow(word):
            word = word.lower()
            if len(word) <= 1:
                return True
            init, *rest = word
            init = combined[init]
            for c in rest:
                if combined[c] != init:
                    return False
            return True
        
        return list ( filter(lambda word: isOneRow(word), words))

# if __name__ == "__main__":
#     print (Solution().findWords("this is a sad time".split(" ")))
        
# @lc code=end

