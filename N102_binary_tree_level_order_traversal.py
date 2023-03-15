from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def inorder(root, level):
            if root:
                if level > len(res)-1:
                    res.append([root.val])
                else:
                    res[level].append(root.val)
                inorder(root.left, level+1)
                inorder(root.right, level+1)

        inorder(root, 0)
        return res