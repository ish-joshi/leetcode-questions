#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def xor(self, a, b):
        return any([a,b]) and (not all([a,b]))

    def helper(self, left, right):
        # one of them is None
        if self.xor(left, right):
            return False
        
        # Both are none
        elif not (left or right):
            return True
        
        # Now both of them have values
        return (left.val == right.val) and ( self.helper(left.left, right.right) 
        and self.helper(left.right, right.left))



    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, root)
        
# @lc code=end

