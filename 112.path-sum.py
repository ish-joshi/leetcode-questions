#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isLeaf(self, node):
        return not (node.left or node.right)

    def pathSum(self, node, target, csum=0):
        """This is a recursive function auxillary helper method. It basically looks out for the computation.
        An edge case I encountered was [1, 2] and the total of 1; Make sure that the node is leaf then only compare
        Otherwise the comparsion is false.

        Args:
            node (TreeNode): some node
            target (int): some path sum that should be reached
            csum (int, optional): Keep track of current sum to help make decision about the path sum. Defaults to 0.

        Returns:
            bool: if a path from root to leaf can be added up to target
        """
        if not node:
            return False

        cnodeval = node.val

        if self.isLeaf(node):
            return (csum + cnodeval) == target

        return self.pathSum(node.left, target, csum + cnodeval) or self.pathSum(node.right, target, csum + cnodeval)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.pathSum(root, sum, 0)
        
# @lc code=end

