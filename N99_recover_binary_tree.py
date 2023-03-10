from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = list()
        a, b = 0, 0

        def inorder(root):
            if root.left:
                inorder(root.left)
            arr.append(root)
            if root.right:
                inorder(root.right)

        inorder(root)

        for i in range(len(arr)-1):
            if arr[i].val > arr[i+1].val:
                a = i
                break

        for i in range(len(arr)-1, 0, -1):
            if arr[i].val < arr[i-1].val:
                b = i
                break

        arr[a].val, arr[b].val = arr[b].val, arr[a].val