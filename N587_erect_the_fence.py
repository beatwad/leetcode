from typing import *
from functools import cmp_to_key


class SolutionChain:
    def calculate_angle(self, t0, t1, t2):
        x0, y0 = t0[0], t0[1]
        x1, y1 = t1[0], t1[1]
        x2, y2 = t2[0], t2[1]
        return (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)

    def outerTrees(self, trees: List[List[int]]) -> List[Tuple[int]]:
        points = sorted(trees)
        lower = []
        upper = []

        for point in points:
            while len(lower) >= 2 and self.calculate_angle(lower[-2], lower[-1], point) > 0:
                lower.pop()
            while len(upper) >= 2 and self.calculate_angle(upper[-2], upper[-1], point) < 0:
                upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))
        return list(set(lower + upper))


class SolutionGraham:
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
        # if the points in the beginning of the tree are on the same level with bottom left point
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
        # search for the convex hull
        for i in range(len(trees)):
            while self.calculate_angle(stack[-2], stack[-1], trees[i]) < 0:
                stack.pop()
            stack.append(trees[i])

        return stack


class SolutionJarvis:
    def leftmost(self, trees):
        leftmost_point = float('inf')
        idx = 0
        for i in range(len(trees)):
            if trees[i][0] < leftmost_point:
                leftmost_point = trees[i][0]
                idx = i
        return idx

    def calculate_angle(self, t0, t1, t2):
        x0, y0 = t0[0], t0[1]
        x1, y1 = t1[0], t1[1]
        x2, y2 = t2[0], t2[1]
        return (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)

    def in_between(self, p, i, q):
        a = (p[0] <= i[0] <= q[0]) or (q[0] <= i[0] <= p[0])
        b = (p[1] <= i[1] <= q[1]) or (q[1] <= i[1] <= p[1])
        return a and b

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # if number of points equal or less than 3 - hull is convex
        if len(trees) <= 3:
            return trees
        # select point with minimum X-coord
        lm_idx = self.leftmost(trees)
        # create stack
        hull = list()
        p = lm_idx
        while True:
            q = (p + 1) % len(trees)
            for i in range(len(trees)):
                if self.calculate_angle(trees[p], trees[i], trees[q]) > 0:
                    q = i
            for i in range(len(trees)):
                if i != p and i != q and \
                        self.calculate_angle(trees[p], trees[i], trees[q]) == 0 and\
                        self.in_between(trees[p], trees[i], trees[q]) and trees[i] not in hull:
                    hull.append(trees[i])
            hull.append(trees[q])
            p = q
            if p == lm_idx:
                break

        return hull


if __name__ == '__main__':
    sol = SolutionChain()
    assert sol.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]) == [(2, 4), (1, 1), (2, 0), (4, 2), (3, 3)]
    assert sol.outerTrees([[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5],
                           [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]) == [(7, 4), (5, 5), (1, 2), (2, 1),
                                                                                        (6, 5), (4, 0), (6, 1), (0, 3),
                                                                                        (1, 4), (3, 0), (7, 3), (4, 5),
                                                                                        (5, 0), (7, 2), (2, 5), (3, 5)]
    sol = SolutionGraham()
    assert sol.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]) == [[2, 0], [4, 2], [3, 3], [2, 4], [1, 1]]
    assert sol.outerTrees([[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5],
                           [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]) == [[3, 0], [4, 0], [5, 0], [6, 1],
                                                                                        [7, 2], [7, 3], [7, 4], [6, 5],
                                                                                        [5, 5], [4, 5], [3, 5], [2, 5],
                                                                                        [1, 4], [0, 3], [1, 2], [2, 1]]
    sol = SolutionJarvis()
    assert sol.outerTrees([[1, 2], [2, 2], [4, 2], [5, 2], [6, 2], [7, 2]]) == [[2, 2], [4, 2], [5, 2], [6, 2],
                                                                                [7, 2], [1, 2]]
    assert sol.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]) == [[2, 0], [4, 2], [3, 3], [2, 4], [1, 1]]
    assert sol.outerTrees([[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5],
                           [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]) == [[1, 2], [2, 1], [3, 0], [4, 0],
                                                                                        [5, 0], [6, 1], [7, 2], [7, 3],
                                                                                        [7, 4], [6, 5], [5, 5], [4, 5],
                                                                                        [3, 5], [2, 5], [1, 4], [0, 3]]
