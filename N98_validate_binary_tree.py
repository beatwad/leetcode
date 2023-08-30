class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def passBST(root):
            if root:
                return passBST(root.left) + [root.val] + passBST(root.right)
            return []

        res = passBST(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True

