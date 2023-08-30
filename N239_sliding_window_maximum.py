from collections import deque
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_deque = deque()
        res = list()
        for i, v in enumerate(nums):
            while max_deque and nums[max_deque[-1]] < v:
                max_deque.pop()
            max_deque.append(i)
            if i < k - 1:
                continue
            if max_deque[0] <= i - k:
                max_deque.popleft()
            res.append(nums[max_deque[0]])
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxSlidingWindow([1], 1) == [1]
    assert sol.maxSlidingWindow([1, 1], 1) == [1, 1]
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow([1, 2], 1) == [1, 2]
    assert sol.maxSlidingWindow([2, 1], 1) == [2, 1]
    assert sol.maxSlidingWindow([1, 2], 2) == [2]
    assert sol.maxSlidingWindow([1, 3, 2], 2) == [3, 3]
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 4) == [3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 8) == [7]
