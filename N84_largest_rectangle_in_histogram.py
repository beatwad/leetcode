from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(-1)
        res = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
