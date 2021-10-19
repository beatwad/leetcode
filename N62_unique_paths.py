class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                arr[j] += arr[j-1]
        return arr[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 3) == 6
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(7, 3) == 28
    assert sol.uniquePaths(1, 1) == 1
