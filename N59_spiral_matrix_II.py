from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for j in range(n)]

        r, c, ri, ci = 0, 0, 0, 1
        for k in range(n**2):
            res[r][c] = k + 1

            if res[(r + ri) % n][(c + ci) % n]:
                ci, ri = -ri, ci

            r += ri
            c += ci

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.generateMatrix(1) == [[1]]
    assert sol.generateMatrix(2) == [[1, 2], [4, 3]]
    assert sol.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert sol.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

