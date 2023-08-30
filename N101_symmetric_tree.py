from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_sub_trees(a, b):
            if a and b:
                return a.val == b.val and check_sub_trees(a.left, b.right) and check_sub_trees(a.right, b.left)
            return a is b

        return check_sub_trees(root.left, root.right)