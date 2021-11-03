class Solution:
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([-5, 1]) == 1
    assert sol.maxSubArray([-5, 1, -2]) == 1
    assert sol.maxSubArray([-5, 1, -2, 2]) == 2
    assert sol.maxSubArray([-5, 1, 1, -2]) == 2
    assert sol.maxSubArray([-2, 1, -3, 4]) == 4
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
