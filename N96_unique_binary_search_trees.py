class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-j-1]
        return res[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.numTrees(1) == 1
    assert sol.numTrees(2) == 2
    assert sol.numTrees(3) == 5
    assert sol.numTrees(4) == 14
    assert sol.numTrees(5) == 42
    assert sol.numTrees(14) == 2674440
    assert sol.numTrees(19) == 1767263190
