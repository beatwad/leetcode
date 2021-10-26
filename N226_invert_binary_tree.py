# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, node_list):
        if node_list:
            self.root = self.build_tree(node_list, 0)
        else:
            self.root = None

    def build_tree(self, node_list: list, i: int):
        root = TreeNode(node_list[i])
        if 2*i + 1 < len(node_list):
            root.left = self.build_tree(node_list, 2*i+1)
        else:
            root.left = None
        if 2*i + 2 < len(node_list):
            root.right = self.build_tree(node_list, 2*i+2)
        else:
            root.right = None
        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def visualize_tree(self, root, level=0):
        if root:
            self.visualize_tree(root.left, level+1)
            print(' ' * 4 * level + '->', root.val)
            self.visualize_tree(root.right, level+1)


if __name__ == '__main__':
    sol = Solution()
    tree = Tree([4, 2, 7, 1, 3, 6, 9, 0, 1, 2, 4, 5, 7, 8, 10])
    sol.invertTree(tree.root)
    sol.visualize_tree(tree.root)
