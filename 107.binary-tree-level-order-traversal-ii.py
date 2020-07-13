#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """Level order traversal usingg BFS. Common technique. Once the level order is done, reverse the list.

        Args:
            root (TreeNode): tree

        Returns:
            List[List[int]]: List of elements for level in reverse order
        """

        if not root:
            return []

        q = deque([root])
        lvls = []

        while q:
            currentlevel = []
            qsize = len(q)

            for _ in range(qsize):
                popped = q.popleft()
                currentlevel.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            
            lvls.append(currentlevel)
        
        return list (reversed(lvls))




        
# @lc code=end

