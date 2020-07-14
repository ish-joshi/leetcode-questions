#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """Check if the robot returns to origin
        The algorithm checks the number of up is the number of down; and left-right;
        Instead of using a dictionary as additional space, a 4 size array could be used.
        Even better, two counter variables could be used and check that they're 0 at the end
        uc += 1 when U, uc -= 1 when D. It'd yield the correct answer that way. 

        Time: O(N)
        Space: O(4) --> the dictionary O(1)

        Args:
            moves (str): UPLR string

        Returns:
            bool: if it returns to origin
        """
        dirstore = Counter(moves)
        up = dirstore.get('U', 0)
        down = dirstore.get('D', 0)
        left = dirstore.get('L', 0)
        right = dirstore.get('R', 0)

        return (up == down) and (left == right)


# @lc code=end

