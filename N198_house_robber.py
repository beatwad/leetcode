class Solution:
    def rob(self, nums: list) -> int:
        dp = [nums[0]] + [0]*(len(nums)-1)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.rob([2, 7, 10, 3, 1]) == 13
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([1]) == 1
    assert sol.rob([1, 2]) == 2
    assert sol.rob([1, 2, 1]) == 2
    assert sol.rob([1, 4, 4]) == 5
    assert sol.rob([5, 1, 4, 4]) == 9
    assert sol.rob([2, 7, 10, 3, 1, 4, 1, 5, 6]) == 22
