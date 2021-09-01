import math


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        three_sum_closeset = math.inf
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == target:
                    return target
                if abs(target-three_sum) < abs(target-three_sum_closeset):
                    three_sum_closeset = three_sum
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
        return three_sum_closeset


if __name__ == '__main__':
    sol = Solution()
    assert sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], -9) == -8
    assert sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 0) == 0
    assert sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 1) == 1
    assert sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 12) == 12
    assert sol.threeSumClosest([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], 17) == 16
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert sol.threeSumClosest([0, 0, 0], 1) == 0
