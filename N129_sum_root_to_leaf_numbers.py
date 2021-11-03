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

    def visualize_tree(self, root, level=0):
        if root:
            self.visualize_tree(root.right, level+1)
            print(' ' * 4 * level + '->', root.val)
            self.visualize_tree(root.left, level+1)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = list()
        self.helper(root, str(root.val), res)
        return sum(res)

    def helper(self, root, val, res):
        if not root.left and not root.right:
            res.append(int(val))
        if root.left:
            self.helper(root.left, val + str(root.left.val), res)
        if root.right:
            self.helper(root.right, val + str(root.right.val), res)


if __name__ == '__main__':
    sol = Solution()
    tree = Tree([0])
    tree.visualize_tree(tree.root)
    assert sol.sumNumbers(tree.root) == 0
    print('#' * 80)
    tree = Tree([1])
    tree.visualize_tree(tree.root)
    assert sol.sumNumbers(tree.root) == 1
    print('#' * 80)
    tree = Tree([1, 2])
    tree.visualize_tree(tree.root)
    print(sol.sumNumbers(tree.root))
    assert sol.sumNumbers(tree.root) == 12
    print('#' * 80)
    tree = Tree([1, 2, 3])
    tree.visualize_tree(tree.root)
    assert sol.sumNumbers(tree.root) == 25
    print('#' * 80)
    tree = Tree([4, 9, 0, 5, 1])
    tree.visualize_tree(tree.root)
    assert sol.sumNumbers(tree.root) == 1026
    print('#' * 80)
    tree = Tree([4, 9, 3, 5, 1, 2])
    tree.visualize_tree(tree.root)
    assert sol.sumNumbers(tree.root) == 1418
