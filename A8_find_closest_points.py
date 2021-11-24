from typing import *
import math


class Solution:
    def find_closest_points(self, points: List[List[int]]) -> Tuple[int, List[int], List[int]]:
        x = sorted(points)
        y = sorted(points, key=lambda i: i[1])

        def dist(p1, p2):
            if not p1 or not p2:
                return float('inf')
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2), p1, p2

        def helper(x, y):
            # check if point array length < 3
            if len(x) < 2:
                return float('inf'), None, None
            if len(x) == 2:
                return dist(x[0], x[1])
            # split point array on two equal subarrays sorted buy x-coord
            x_l = x[:len(x)//2]
            x_r = x[len(x)//2:]
            # split point array on two equal subarrays sorted by y-coords
            y_l = list()
            y_r = list()
            for v in y:
                if v in x_l:
                    y_l.append(v)
                else:
                    y_r.append(v)
            # find minimal distance for both arrays
            dist_l, p1_l, p2_l = helper(x_l, y_l)
            dist_r, p1_r, p2_r = helper(x_r, y_r)
            if dist_l <= dist_r:
                min_dist, p1, p2 = dist_l, p1_l, p2_l
            else:
                min_dist, p1, p2 = dist_r, p1_r, p2_r
            # find all points that lies close to border line
            mid_x = x[len(x)//2][0]
            # find min distance for each point in that array and each of 8 point behind that point in array p
            y_m = list()
            for v in x:
                if (mid_x - min_dist) <= v[0] <= (mid_x + min_dist):
                    y_m.append(v)
            for v in y_m:
                idx = x.index(v)
                for w in x[idx+1:idx+8]:
                    d = dist(v, w)[0]
                    if d < min_dist:
                        min_dist = d
                        p1 = v
                        p2 = w
            return min_dist, p1, p2

        return helper(x, y)


if __name__ == '__main__':
    sol = Solution()
    assert sol.find_closest_points([[-2, -2], [0, 0], [1, 1], [3, 3]]) == (math.sqrt(2), [0, 0], [1, 1])
    assert sol.find_closest_points([[-2.5, -2], [-2, -2], [0, 0], [1, 1], [3, 3]]) == (0.5, [-2.5, -2], [-2, -2])
    assert sol.find_closest_points([[-2.5, -2], [-2, -2], [0, 0], [0.3, 0], [1, 1], [3, 3]]) == (0.3, [0, 0], [0.3, 0])

