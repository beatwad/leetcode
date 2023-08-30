from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        null_flag = False

        while level:
            tmp = list()

            for node in level:
                if node is None:
                    null_flag = True
                elif null_flag:
                    return False
                else:
                    tmp.append(node.left)
                    tmp.append(node.right)
            level = tmp.copy()

        return True