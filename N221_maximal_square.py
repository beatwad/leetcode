class Solution:
    def maximalSquare(self, matrix: list) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_res, prev = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]) + 1
                    max_res = max(dp[i][j], max_res)
        return max_res**2


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximalSquare([["0"]]) == 0
    assert sol.maximalSquare([["0", "0"],
                              ["0", "0"]]) == 0
    assert sol.maximalSquare([["1", "0"],
                              ["1", "0"]]) == 1
    assert sol.maximalSquare([["0", "1"],
                              ["1", "0"]]) == 1
    assert sol.maximalSquare([["1", "1"],
                              ["1", "0"]]) == 1
    assert sol.maximalSquare([["1", "1"],
                              ["1", "1"]]) == 4
    assert sol.maximalSquare([["1", "1", "0"],
                              ["1", "1", "0"]]) == 4
    assert sol.maximalSquare([["0", "1", "0"],
                              ["1", "1", "0"]]) == 1
    assert sol.maximalSquare([["1", "1", "1", "0"],
                              ["1", "1", "1", "0"],
                              ["0", "0", "0", "0"]]) == 4
    assert sol.maximalSquare([["1", "0", "1", "0", "0"],
                              ["1", "0", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"],
                              ["1", "0", "0", "1", "0"]]) == 4
    assert sol.maximalSquare([["1", "1", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"],
                              ["0", "0", "0", "0", "0"],
                              ["1", "1", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"]]) == 4
    assert sol.maximalSquare([["1", "0", "1", "0", "0"],
                              ["1", "0", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"],
                              ["1", "0", "1", "1", "1"]]) == 9
    assert sol.maximalSquare([["1", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"],
                              ["0", "0", "1", "1", "1"]]) == 16
