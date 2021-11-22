class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    sol = Solution()
    assert sol.hammingDistance(0, 0) == 0
    assert sol.hammingDistance(0, 1) == 1
    assert sol.hammingDistance(1, 4) == 2
    assert sol.hammingDistance(5, 6) == 2
    assert sol.hammingDistance(6, 9) == 4
    assert sol.hammingDistance(345, 345) == 0
    assert sol.hammingDistance(344, 345) == 1
    assert sol.hammingDistance(153533, 4565353) == 15
