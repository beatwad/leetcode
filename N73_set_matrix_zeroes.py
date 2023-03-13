from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_zeroes, col_zeroes = [], []

        for i in range(m):
            if 0 in matrix[i]:
                row_zeroes.append(i)

        for j in range(n):
            if 0 in [m[j] for m in matrix]:
                col_zeroes.append(j)

        for i in row_zeroes:
            matrix[i] = [0] * n

        for i in range(m):
            if i in row_zeroes:
                continue
            for j in col_zeroes:
                matrix[i][j] = 0


if __name__ == '__main__':
    sol = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
