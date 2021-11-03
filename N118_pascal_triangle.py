class Solution:
    def generate(self, numRows: int) -> list:
        arr = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr


if __name__ == '__main__':
    sol = Solution()
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]
    assert sol.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert sol.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
