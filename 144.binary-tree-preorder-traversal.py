#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

"""
   1
2     3

1 + pO(2) + pO(3)
1 + 2 + _ + _ + pO(3)
1 + 2 + _ + _ + 3 + pO(None) + pO(None)
1 + 2 + _ + _ + 3 + _ + _
[1 + 2 + 3]



"""
        
# @lc code=end

