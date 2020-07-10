#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
from typing import List
class Solution:
    """Checks if the word can be constructed with one row in the keyboard.
    Proud of how I constructed the dictionary to map the rows. 
    """
    def findWords(self, words: List[str]) -> List[str]:

        row1 = {c:1 for c in list("qwertyuiop")}
        row2 = {c:2 for c in list("asdfghjkl")}
        row3 = {c:3 for c in list("zxcvbnm")}

        # map of {a: 2, q: 1, z: 3, ....}
        combined = {**row1, **row2, **row3}
        # print(combined)

        def isOneRow(word):
            """Check if one word in isolation is part of one row. 
            breaking down the problem

            Args:
                word (string): a word in a list. Is converted to lowercase for comaprsion.

            Returns:
                boolean: indicating if the word is constructed in one row
            """
            word = word.lower()
            if len(word) <= 1:
                return True
            init, *rest = word
            init = combined[init]
            for c in rest:
                if combined[c] != init:
                    return False
            return True
        
        # Simple filter to use the previous function
        return list ( filter(lambda word: isOneRow(word), words))

# if __name__ == "__main__":
#     print (Solution().findWords("this is a sad time".split(" ")))
        
# @lc code=end

