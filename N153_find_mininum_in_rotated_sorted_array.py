class Solution:
    def findMin(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        l, m, r = 0, 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m] and nums[m+1] <= nums[r]:
                return min([nums[l], nums[m+1]])
            elif nums[l] > nums[m]:
                r = m
            else:
                l = m + 1


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMin([3]) == 3
    assert sol.findMin([3, 1]) == 1
    assert sol.findMin([1, 3]) == 1
    assert sol.findMin([3, 1, 2]) == 1
    assert sol.findMin([-5, 1, 2]) == -5
    assert sol.findMin([3, 4, 1, 2]) == 1
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([3, 4, 5, 6, 0, 1, 2]) == 0
    assert sol.findMin([7, 8, 1, 2, 3, 4, 5, 6]) == 1
    assert sol.findMin([3, 4, 5, 6, -3, -2, -1, 0, 1, 2]) == -3
    assert sol.findMin([11, 13, 15, 17]) == 11
    assert sol.findMin([11, 13, 15, 17, -11]) == -11
