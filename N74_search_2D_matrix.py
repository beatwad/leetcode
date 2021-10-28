class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        # binary search row
        l, r = 0, len(matrix)-1
        while l <= r:
            t_row = l + (r-l) // 2
            if target == matrix[t_row][0]:
                return True
            elif matrix[t_row][0] < target <= matrix[t_row][-1]:
                break
            elif target > matrix[t_row][0]:
                l = t_row + 1
            else:
                r = t_row - 1
        else:
            return False
        # binary search for target in row
        l, r = 0, len(matrix[t_row])-1
        while l <= r:
            m = l + (r-l) // 2
            if target == matrix[t_row][m]:
                return True
            elif target > matrix[t_row][m]:
                l = m + 1
            else:
                r = m - 1
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.searchMatrix([[1]], 1) is True
    assert sol.searchMatrix([[1]], 2) is False
    assert sol.searchMatrix([[1, 2]], 2) is True
    assert sol.searchMatrix([[1, 2]], 1) is True
    assert sol.searchMatrix([[1, 2]], 3) is False
    assert sol.searchMatrix([[1], [2]], 1) is True
    assert sol.searchMatrix([[1], [2]], 2) is True
    assert sol.searchMatrix([[1], [2]], 3) is False
    assert sol.searchMatrix([[1, 2], [3, 4]], 2) is True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 2) is False
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1) is True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60) is True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 34) is True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 31) is False
