# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> list:
        tree_dict = dict()

        def tree_walk(root):
            if root.val in tree_dict:
                tree_dict[root.val] += 1
            else:
                tree_dict[root.val] = 1
            if root.left:
                tree_walk(root.left)
            if root.right:
                tree_walk(root.right)

        tree_walk(root)
        mode_value = max(tree_dict.values())
        res = [k for k in tree_dict if tree_dict[k] == mode_value]
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(3)

    #           1
    #          / \
    #       null  2
    #            / \
    #           2   3
    #                \
    #                 3

    sol = Solution()
    assert sol.findMode(root) == [2, 3]
