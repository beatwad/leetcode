class Solution:
    def getRow(self, rowIndex: int) -> list:
        arr = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1, 1]
    assert sol.getRow(2) == [1, 2, 1]
    assert sol.getRow(3) == [1, 3, 3, 1]
    assert sol.getRow(4) == [1, 4, 6, 4, 1]
    assert sol.getRow(5) == [1, 5, 10, 10, 5, 1]
