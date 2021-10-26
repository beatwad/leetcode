class Solution:
    def mySqrt(self, x: int) -> int:
        a = x // 2
        prev_a = a
        while True:
            if a**2 == x or a**2 < x <= (a+1)**2:
                return a
            if a**2 < x:
                a = a + (prev_a - a) // 2
            else:
                prev_a = a
                a = a // 2


if __name__ == '__main__':
    sol = Solution()
    # assert sol.mySqrt(0) == 0
    assert sol.mySqrt(1) == 1
    # assert sol.mySqrt(8) == 2
    # assert sol.mySqrt(4) == 2
    # assert sol.mySqrt(25) == 5



