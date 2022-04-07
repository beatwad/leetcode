from typing import *
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        gains = Counter(nums)
        max_number = max(gains.keys())
        for k, v in gains.items():
            gains[k] *= k

        max_sums = [0 for _ in range(max_number+1)]
        max_sums[1] = gains[1]

        for i in range(2, max_number+1):
            max_sums[i] = max(max_sums[i-1], max_sums[i-2] + gains[i])

        return max_sums[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.deleteAndEarn([3, 4, 2]) == 6
    assert sol.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
