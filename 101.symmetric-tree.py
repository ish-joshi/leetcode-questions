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
    """Checks if trees are symmetric. It is a recursive problem by default. 
    Check if the left is equal to right while traversing from root. 
    It checks the truth table 00, 01, 10, 11
    00 = True (both are empty)
    01, 10 = False (they're not same)
    11 = Compare + the result of it's children

    The iterative approach is kind of similar. The iterative approach relies on a
    BFS where each level must be a palindrone, with the null. Each null child must 
    add the left and right in the next level as null. Basically assert each level is a 
    palindrone and it will be symmetric that way. 

    """

    def xor(self, a, b):
        """A useful helper function takes in two variables and returns the xor
        They can be objects that may have a type or None. None = False, object = True

        Args:
            a (Booleanish): an object or None
            b (Booleanish): an object or None

        Returns:
            bool: the XOR operation on a and b
        """
        # O(1)
        return any([a,b]) and (not all([a,b]))

    def helper(self, left, right):
        """Uses an aux method to keep two references for the root. It would have been 
        tricky to do it in the driver method. The driver method handles the root being 
        None case. 

        Args:
            left (Node | None): left reference
            right (Node | None): right reference

        Returns:
            bool: the symmetry being valid
        """
        # one of them is None
        if self.xor(left, right):
            return False
        
        # Both are none
        elif not (left or right):
            return True
        
        if left.val != right.val:
            return False
        
        # The values are equal so move on :)

        # Now both of them have values
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)



    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, root)
        
# @lc code=end

