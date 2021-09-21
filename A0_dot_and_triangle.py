class Solution:
    def dot_and_triangle(self, t1: list, t2: list, t3: list, d: list):
        for a, b, c in [[t1, t2, t3], [t2, t1, t3], [t3, t1, t2]]:
            v_product_1 = (b[0]-a[0]) * (d[1]-b[1]) - (b[1]-a[1]) * (d[0]-b[0])
            v_product_2 = (c[0]-a[0]) * (d[1]-c[1]) - (c[1]-a[1]) * (d[0]-c[0])
            if (v_product_1 > 0 and v_product_2 > 0) or (v_product_1 < 0 and v_product_2 < 0):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [2, 3]) is True
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [3, 2]) is True
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [1, 1]) is True
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [2, 2]) is True
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [4, 1]) is False
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [3, 1]) is False
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [5, 4]) is False
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [0, 0]) is False
    assert sol.dot_and_triangle([1, 1], [1, 5], [4, 2], [10, 10]) is False

