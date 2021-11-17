class Solution:
    def rob(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1, dp2 = [0] * (len(nums)-1), [0] * (len(nums)-1)
        dp1[0], dp2[0] = nums[0], nums[1]
        for i in range(1, len(nums)-1):
            dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
            dp2[i] = max(dp2[i-1], nums[i+1] + dp2[i-2])
        return max(dp1[-1], dp2[-1])


if __name__ == '__main__':
    sol = Solution()
    assert sol.rob([2]) == 2
    assert sol.rob([0, 2]) == 2
    assert sol.rob([2, 2]) == 2
    assert sol.rob([2, 3]) == 3
    assert sol.rob([0, 2, 3]) == 3
    assert sol.rob([2, 3, 2]) == 3
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([1, 2, 3]) == 3
