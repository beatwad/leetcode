class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cur = [0 for _ in range(n)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            cur[i] = 1
        for i in range(1, m):
            cur[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, n):
                cur[j] = (cur[j] + cur[j-1]) * (1 - obstacleGrid[i][j])
        return cur[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePathsWithObstacles([[1, 0, 0], [0, 1, 0], [0, 0, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 1]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 0, 0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 1, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 1, 0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 2
    assert sol.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]) == 5
    assert sol.uniquePathsWithObstacles([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 1], [1, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 1], [0, 1]]) == 0
    assert sol.uniquePathsWithObstacles([[0, 1], [1, 0], [0, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0]]) == 1
    assert sol.uniquePathsWithObstacles([[1]]) == 0
    assert sol.uniquePathsWithObstacles([[0], [0]]) == 1
    assert sol.uniquePathsWithObstacles([[0], [0], [0]]) == 1
    assert sol.uniquePathsWithObstacles([[0, 1, 0]]) == 0
    assert sol.uniquePathsWithObstacles([[0], [1], [1], [0]]) == 0
    assert sol.uniquePathsWithObstacles([[0], [1], [0]]) == 0
    assert sol.uniquePathsWithObstacles([[0], [1]]) == 0
