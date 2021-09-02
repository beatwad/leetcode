from itertools import product

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list:

        def helper(begin, end):
            if begin > end:
                return [None]

            if begin == end:
                return [TreeNode(begin)]

            res = list()

            for i in range(begin, end+1):
                left = helper(begin, i-1)
                right = helper(i+1, end)
                for pair in product(left, right):
                    res.append(TreeNode(i, pair[0], pair[1]))

            return res

        res = helper(1, n)
        return res




