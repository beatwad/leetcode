class Solution:
    def maxProduct(self, nums: list) -> int:
        global_max = prev_max = prev_min = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            curr_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxProduct([-2]) == -2
    assert sol.maxProduct([2]) == 2
    assert sol.maxProduct([2, 2]) == 4
    assert sol.maxProduct([2, -1, 2]) == 2
    assert sol.maxProduct([-2, 3, -4]) == 24
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([2, 3, -2, 4, 2]) == 8
    assert sol.maxProduct([-2, 0, -2]) == 0
    assert sol.maxProduct([1, 2, 3, 4]) == 24
    assert sol.maxProduct([2, -5, -2, -4, 3]) == 24
    assert sol.maxProduct([1, -2, 3, 4, -1]) == 24
    assert sol.maxProduct([1, 0, -1, 2, 3, -5, -2]) == 60
    assert sol.maxProduct([1, -2, 3, 4, -1, 10]) == 240
