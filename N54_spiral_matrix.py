class Solution:
    def spiralOrder(self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])
        seen = [[0 for _ in range(n)] for __ in range(m)]
        res = []
        dir_i = [0, 1, 0, -1]
        dir_j = [1, 0, -1, 0]
        i, j, k, count = 0, 0, 0, 0
        for _ in range(m*n):
            res.append(matrix[i][j])
            seen[i][j] = 1
            if not (0 <= i+dir_i[k] < m and 0 <= j+dir_j[k] < n and seen[i+dir_i[k]][j+dir_j[k]] == 0):
                k = (k + 1) % 4
            i += dir_i[k]
            j += dir_j[k]
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
