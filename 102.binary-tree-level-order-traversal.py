#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        
        out = []

        q = deque([root])

        while q:

            thisLevel = []
            levelSize = len(q)

            for _ in range (levelSize):
                
                popped = q.popleft()

                thisLevel.append(popped.val)

                # Only add if it's not none
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            
            out.append(thisLevel)
        
        return out






        
# @lc code=end

