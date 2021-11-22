from typing import *
from functools import cmp_to_key


class Solution:
    def bottom_left(self, trees):
        min_y = min([t[1] for t in trees])
        min_x = min([t[0] for t in trees if t[1] == min_y])
        first_point = [min_x, min_y]
        return first_point

    def calculate_angle(self, t0, t1, t2):
        x0, y0 = t0[0], t0[1]
        x1, y1 = t1[0], t1[1]
        x2, y2 = t2[0], t2[1]
        return (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)

    def calculate_dist(self, t1, t2):
        x1, y1 = t1[0], t1[1]
        x2, y2 = t2[0], t2[1]
        return (x1-x2)**2 + (y1-y2)**2

    def compare(self, t1, t2):
        global bl
        prod = self.calculate_angle(bl, t1, t2)
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        elif self.calculate_dist(bl, t1) - self.calculate_dist(bl, t2) > 0:
            return 1
        return -1

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        global bl
        # if number of points equal or less than 3 - hull is convex
        if len(trees) <= 3:
            return trees
        # select point with minimum X-coord
        # trees = sorted(trees, key=lambda x: x[0])
        bl = self.bottom_left(trees)
        # sort all the rest points in list according to their polar angle
        trees = sorted([t for t in trees if t != bl], key=cmp_to_key(self.compare), reverse=True)
        # if the points in the begining of the tree are on the same level with bottom left point
        # sort them by distance from bottom left
        i = 1
        while i < len(trees)-1 and self.calculate_angle(bl, trees[i-1], trees[i]) == 0:
            i += 1
        trees_reversed = trees[:i][::-1]
        trees = trees_reversed + trees[i:]
        # create stack
        stack = list()
        # add first 3 elements
        stack.append(bl)
        stack.append(trees.pop(0))
        stack.append(trees.pop(0))
        for i in range(len(trees)):
            while self.calculate_angle(stack[-2], stack[-1], trees[i]) < 0:
                stack.pop()
            stack.append(trees[i])

        return stack


if __name__ == '__main__':
    sol = Solution()
    assert sol.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]) == [[2, 0], [4, 2], [3, 3], [2, 4], [1, 1]]
    assert sol.outerTrees([[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5],
                           [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]) == [[3, 0], [4, 0], [5, 0], [6, 1],
                                                                                        [7, 2], [7, 3], [7, 4], [6, 5],
                                                                                        [5, 5], [4, 5], [3, 5], [2, 5],
                                                                                        [1, 4], [0, 3], [1, 2], [2, 1]]
