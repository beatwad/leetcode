from typing import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones[-2], stones[-1]
            if x == y:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [y-x]
        if len(stones) == 0:
            return 0
        return stones[0]


if __name__ == '__main__':
    sol = Solution()
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([1, 2, 3]) == 0
    assert sol.lastStoneWeight([1, 1, 1, 1]) == 0
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1, 2, 7, 2, 1, 9, 2, 56, 11, 867, 32, 376, 12, 675, 12, 54, 777, 23,
                                786, 211, 24, 434, 124, 124, 943, 33, 245, 234, 544]) == 1
