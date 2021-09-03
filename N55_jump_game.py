class Solution:
    def jump(self, nums: list) -> bool:
        if 0 not in nums:
            return True
        cur_jump = max_jump = 0
        for i in range(len(nums)):
            max_jump = max(max_jump, nums[i]+i)
            if i > cur_jump:
                return False
            if i == cur_jump:
                cur_jump = max_jump
        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.jump([0]) is True
    assert sol.jump([1]) is True
    assert sol.jump([1, 1]) is True
    assert sol.jump([0, 1]) is False
    assert sol.jump([1, 0]) is True
    assert sol.jump([1, 1, 0]) is True
    assert sol.jump([1, 1, 0, 1]) is False
    assert sol.jump([2, 3, 0, 1, 4]) is True
    assert sol.jump([3, 2, 1, 0, 4]) is False