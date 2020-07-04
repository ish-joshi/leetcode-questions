#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = list ( filter (lambda i: (ord('a') <= ord(i) <= ord('z')) or (ord('0') <= ord(i) <= ord('9')), s))
        s = "".join(s)
        return s == s[::-1]
        
# @lc code=end

