class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list) -> int:

        res = 0
        mines = {tuple(mine) for mine in mines}
        arr = [[0] * n for _ in range(n)]

        for r in range(n):
            # left
            count = 0
            for c in range(n):
                count = 0 if (r, c) in mines else count + 1
                arr[r][c] = count

            # right
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in mines else count + 1
                arr[r][c] = min(arr[r][c], count)

        for c in range(n):
            # down
            count = 0
            for r in range(n):
                count = 0 if (r, c) in mines else count + 1
                arr[r][c] = min(arr[r][c], count)

            # up
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in mines else count + 1
                arr[r][c] = min(arr[r][c], count)
                res = max(res, arr[r][c])

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.orderOfLargestPlusSign(1, [[0, 0]]) == 0
    assert sol.orderOfLargestPlusSign(1, []) == 1
    assert sol.orderOfLargestPlusSign(2, [[0, 0]]) == 1
    assert sol.orderOfLargestPlusSign(2, []) == 1
    assert sol.orderOfLargestPlusSign(5, []) == 3
    assert sol.orderOfLargestPlusSign(5, [[2, 2], [4, 2]]) == 2
    assert sol.orderOfLargestPlusSign(5, [[4, 2]]) == 2
    assert sol.orderOfLargestPlusSign(6, []) == 3
    assert sol.orderOfLargestPlusSign(6, [[5, 2]]) == 3
    assert sol.orderOfLargestPlusSign(6, [[5, 2]]) == 3
    assert sol.orderOfLargestPlusSign(7, [[2, 2], [2, 4], [4, 2], [4, 4]]) == 4
    assert sol.orderOfLargestPlusSign(7, [[2, 2], [2, 4], [4, 2], [4, 4], [3, 3]]) == 2
    assert sol.orderOfLargestPlusSign(20, [[0, 4], [0, 7], [0, 11], [0, 12], [0,15], [2, 2], [3, 17], [4, 0], [4, 14],
                                           [5, 9], [5, 19], [6, 10], [6, 16], [6, 17], [7, 13], [8, 0], [8, 1], [8, 6],
                                           [9, 17], [10, 2], [10, 7], [10, 12], [11, 2], [11, 5], [11, 13], [11, 14],
                                           [11, 16], [13, 3], [13, 7], [13, 13], [14, 4], [14, 16], [15, 2], [16, 3],
                                           [16, 12], [17, 2], [17, 9], [17, 13], [17, 14], [17, 18], [19, 5], [19, 11],
                                           [19, 15]]) == 9
