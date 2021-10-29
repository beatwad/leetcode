class Solution:
    def orangesRotting(self, grid: list) -> int:
        stack = list()
        n = len(grid)
        m = len(grid[0])
        # find the rotten orange with the most number of adjacent fresh oranges
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 2:
                    stack.append((x, y))
        # array for minutes amount tracking
        res = [[0] * m for _ in range(n)]
        # find the number of minutes that is needed for all oranges to become rotten
        while stack:
            x, y = stack.pop(0)
            for i, j in [[max(0, x-1), y], [min(x+1, n-1), y], [x, max(0, y-1)], [x, min(y+1, m-1)]]:
                if (i != x or j != y) and grid[i][j] == 1:
                    stack.append((i, j))
                    grid[i][j] = 2
                    res[i][j] = res[x][y] + 1
        # if there are still fresh oranges - return -1
        for i in range(n):
            if 1 in grid[i]:
                return -1
        return max(sum(res, []))


if __name__ == '__main__':
    sol = Solution()
    # print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    assert sol.orangesRotting([[0]]) == 0
    assert sol.orangesRotting([[1]]) == -1
    assert sol.orangesRotting([[2]]) == 0
    assert sol.orangesRotting([[2, 2]]) == 0
    assert sol.orangesRotting([[2, 2], [2, 1]]) == 1
    assert sol.orangesRotting([[2, 2], [2, 2]]) == 0
    assert sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    assert sol.orangesRotting([[1, 2]]) == 1
    assert sol.orangesRotting([[1], [2]]) == 1
    assert sol.orangesRotting([[0], [2]]) == 0
    assert sol.orangesRotting([[1, 1], [1, 2]]) == 2
    assert sol.orangesRotting([[1, 1], [1, 1], [1, 2]]) == 3
    assert sol.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
