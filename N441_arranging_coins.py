import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        steps = int((math.sqrt(8*n+1) - 1)/2)
        return steps


if __name__ == '__main__':
    sol = Solution()
    assert sol.arrangeCoins(1) == 1
    assert sol.arrangeCoins(2) == 1
    assert sol.arrangeCoins(5) == 2
    assert sol.arrangeCoins(8) == 3
