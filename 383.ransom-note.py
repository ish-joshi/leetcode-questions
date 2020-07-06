#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notec = collections.Counter(ransomNote)
        magc = collections.Counter(magazine)

        # notec <= magc

        for key, value in notec.items():

            # Character does not exist in magazien
            if magc.get(key) is None:
                return False
            
            # See if magazine is less
            if magc.get(key) < value:
                return False
        
        return True


# @lc code=end

