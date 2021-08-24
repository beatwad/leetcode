class Solution:
    def max_area(self, height: list) -> int:
        n = len(height)
        l, r = 0, n-1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > res:
                res = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == '__main__':
    sol = Solution()

    assert sol.max_area([0, 0]) == 0
    assert sol.max_area([1, 1]) == 1
    assert sol.max_area([1, 8]) == 1
    assert sol.max_area([0, 1, 0]) == 0
    assert sol.max_area([2, 0, 2]) == 4
    assert sol.max_area([1, 2, 1]) == 2
    assert sol.max_area([4, 3, 2, 1, 4]) == 16
    assert sol.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.max_area([1, 9, 6, 2, 5, 4, 3, 9, 7]) == 54
    assert sol.max_area([10, 8, 6, 2, 5, 4, 8, 3, 7]) == 56
    assert sol.max_area([6, 15, 6, 2, 5, 4, 8, 16, 7]) == 90

