class Solution:
    def fourSum(self, nums: list, target):
        four_sum_list = []
        nums.sort()
        for i, num in enumerate(nums[:-3]):
            if i > 0 and num == nums[i - 1]:
                continue
            result = self.threeSum(nums[i+1:], target-num)
            if result:
                for j in result:
                    j = [num] + j
                    four_sum_list.append(j)
        return four_sum_list

    def threeSum(self, nums: list, target: int) -> list:
        three_sum_list = []
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < target:
                    l += 1
                elif three_sum > target:
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

    assert sol.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sol.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]


