class Solution:
    def minimumTotal(self, triangle: list) -> int:
        n = len(triangle)
        for i in range(1, n):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[n-1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.minimumTotal([[-10]]) == -10
    assert sol.minimumTotal([[1], [2, 3]]) == 3
    assert sol.minimumTotal([[1], [2, 3], [7, 22, 1]]) == 5
    assert sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 3, 8, 3]]) == 13
    assert sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 3, 8, 3], [4, 8, 1, 2, 5]]) == 14
