#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        """Interesting algorithm; suprised this question is downvoted a lot;
        Basically running a compression (basic basic) to merge consecutive characters
        together; Similar techniques can be applied to many different solutions;

        It is similar to a question I've screwed up in a Google interview before.

        I misread the question and apprantly it involves doing an in-place transformation;
        that is the reason why it is under voted. 

        #TODO: inplace fixing of the array

        
        Args:
            chars (List[str]): a string as a list

        Returns:
            int: the # of characters needed
        """

        slen = len(chars)

        # aa ab ba bb so a2 is still 2 and if not same it's still 2 :)
        if slen < 3:
            return slen





        
# @lc code=end

