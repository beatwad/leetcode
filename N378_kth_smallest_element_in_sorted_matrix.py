from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0])
        left, right = matrix[0][0], matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            count = 0

            for i in range(n):
                j = 0
                while j < n and matrix[i][j] <= mid:
                    j += 1
                count += j

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    sol = Solution()
    # assert sol.kthSmallest([[1, 1], [1, 1]], 2) == 1
    # assert sol.kthSmallest([[1, 2], [1, 3]], 2) == 1
    assert sol.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6) == 11
    assert sol.kthSmallest([[1, 5, 9, 10], [10, 11, 13, 14], [12, 13, 15, 19], [20, 21, 22, 25]], 1) == 1
    assert sol.kthSmallest([[1, 5, 9, 10], [10, 11, 13, 14], [12, 13, 15, 19], [20, 21, 22, 25]], 14) == 21
    assert sol.kthSmallest([[1, 5, 9, 10], [10, 11, 13, 14], [12, 13, 15, 19], [20, 21, 22, 25]], 16) == 25
