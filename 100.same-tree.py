#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
        return (not all([a,b])) and (any([a,b]))

    def sameRecursive(self, p, q):
        if self.xor(p,q):
            return False # Only one of them is None type. 
        
        if not (p or q):
            # both are None
            return True
        
        # at this point both have some values
        bothEqual = p.val == q.val

        if not bothEqual:
            return False # I know this check is redundant as the next condition would would in the return
            # statement
        
        return bothEqual and (self.sameRecursive(p.left, q.left) and self.sameRecursive(p.right, q.right))

        


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Check if two treenodes are the same tree
        There are two main approaches that come to mind.
        1. Use recursion to traverse both trees in sync. If they go out of sync
        return False. If the whole traversal succeeds, then output True.
        
        2. Do a breadth first search with nulls. Check if the two queues are the same at each level.
        If the queues differ, then the trees are different. If whole traversal succeeds then
        output true.

        Args:
            p (TreeNode): tree 1
            q (TreeNode): tree 2

        Returns:
            bool: if tree 1 is the same as tree
        """

        return self.sameRecursive(p, q)
        
# @lc code=end

