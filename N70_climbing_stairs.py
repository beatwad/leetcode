class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = f2 = 1
        for i in range(n-1):
            f1, f2 = f1 + f2, f1
        return f1


if __name__ == '__main__':
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(4) == 5
