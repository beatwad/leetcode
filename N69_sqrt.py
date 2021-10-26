class Solution:
    def mySqrt(self, x: int) -> int:
        a = x // 2
        while True:
            if a**2 == x or a**2 < x < (a+1)**2:
                return a
            if a**2 < x:
                a = 3*a // 2
            else:
                a = a // 2


if __name__ == '__main__':
    sol = Solution()
    assert sol.mySqrt(25) == 5



