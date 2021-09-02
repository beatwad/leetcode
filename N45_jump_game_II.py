class Solution:
    def jump(self, nums: list) -> int:
        n = len(nums)
        cur_max_jump = next_max_jump = res = 0
        for i in range(n-1):
            next_max_jump = max(nums[i]+i, next_max_jump)
            if i == cur_max_jump:
                res += 1
                cur_max_jump = next_max_jump
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.jump([0]) == 0
    assert sol.jump([1]) == 0
    assert sol.jump([1, 1]) == 1
    assert sol.jump([2, 1]) == 1
    assert sol.jump([2, 3, 1]) == 1
    assert sol.jump([1, 3, 1]) == 2
    assert sol.jump([2, 0, 2, 0, 1]) == 2
    assert sol.jump([1, 2, 1, 1, 1]) == 3
    assert sol.jump([1, 1, 1, 1, 1]) == 4
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
