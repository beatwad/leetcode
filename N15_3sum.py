class Solution:
    def threeSum(self, nums: list) -> list:
        three_sum_list = []
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res = [nums[i], nums[l], nums[r]]
                    three_sum_list.append(res)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return three_sum_list


if __name__ == '__main__':
    sol = Solution()
    assert sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [(-4, 1, 3),
                                                                               (-4, -2, 6),
                                                                               (-4, 2, 2),
                                                                               (-2, -2, 4),
                                                                               (-4, 0, 4),
                                                                               (-2, 0, 2)]
    assert sol.threeSum([-2, 0, 1, 1, 2]) == [(-2, 0, 2), (-2, 1, 1)]
    assert sol.threeSum([-1, -1, 0, 1, 1, 2]) == [(-1, 0, 1), (-1, -1, 2)]
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [(-1, 0, 1), (-1, -1, 2)]
    assert sol.threeSum([]) == []
    assert sol.threeSum([0]) == []
    assert sol.threeSum([0, 1]) == []
    assert sol.threeSum([0, 0, 0, 0]) == [(0, 0, 0)]
