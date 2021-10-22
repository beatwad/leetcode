class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.minPathSum([[1]]) == 1
    assert sol.minPathSum([[2]]) == 2
    assert sol.minPathSum([[1], [2]]) == 3
    assert sol.minPathSum([[1, 2]]) == 3
    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
