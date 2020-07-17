#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    paths = []

    def isLeaf(self, node):
        if not node:
            return False
        return not (node.left or node.right)

    def constructPaths(self, partial, node):
        """Generates all paths and prints it to the console

        If the Node is None, we've hit a dead end so return back

           1
          / \
             2 

        We're always looking out for the 'leaf' nodes
        Check if the node is leaf. If the node is leaf, add to the self.paths list
        Otherwise keep generating paths in left or right


        Args:
            partial (list): a partially constructed path (potentially)
            node (TreeNode | None): a tree node or none
        """

        if not node:
            return
        
        partial = partial + [node.val]

        if self.isLeaf(node):
            # print("Found path ", partial)
            num = "".join([str(i) for i in partial])
            self.paths.append(int(num))
        else:
            self.constructPaths([i for i in partial], node.left)
            self.constructPaths([i for i in partial], node.right)


    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.paths = [] # this must be resest across leetcode answers :(
        self.constructPaths([], root)
        print(self.paths)
        return sum(self.paths)
        
# @lc code=end

