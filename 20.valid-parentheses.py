#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        openings = "(,{,[".split(",")
        matching = {")": "(", "}": "{", "]": "["}

        print(openings, matching)

        st = []

        for c in s:
            if c in openings:
                st.append(c)
            else:
                if len(st) <= 0:
                    return False

                pped = st.pop()
                if matching[c] != pped:
                    return False
        
        return len(st) == 0

        
# @lc code=end