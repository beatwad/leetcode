from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        res = 0

        while l <= r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)

            if lmax <= rmax:
                res += lmax - height[l]
                l += 1
            else:
                res += rmax - height[r]
                r -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.trap([1]) == 0
    assert sol.trap([1, 10]) == 0
    assert sol.trap([1, 0, 2]) == 1
    assert sol.trap([1, 0, 0, 2]) == 2
    assert sol.trap([2, 0, 0, 2]) == 4
    assert sol.trap([3, 0, 0, 2]) == 4
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    assert sol.trap([5, 4, 3, 2, 1]) == 0
