class Solution:
    def mySqrt(self, x: int) -> int:
        ans, low, high = 0, 0, x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    assert sol.mySqrt(0) == 0
    assert sol.mySqrt(1) == 1
    assert sol.mySqrt(2) == 1
    assert sol.mySqrt(8) == 2
    assert sol.mySqrt(4) == 2
    assert sol.mySqrt(25) == 5
    assert sol.mySqrt(169) == 13
    assert sol.mySqrt(1369) == 37
    assert sol.mySqrt(1370) == 37
    assert sol.mySqrt(2**31-1) == 46340



