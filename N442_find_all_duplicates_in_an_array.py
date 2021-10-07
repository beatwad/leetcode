class Solution:
    def findDuplicates(self, nums: list) -> list:
        res = []
        for num in nums:
            num = abs(num)
            if nums[num-1] > 0:
                nums[num-1] = -nums[num-1]
            else:
                res.append(num)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.findDuplicates([5, 4, 6, 7, 9, 3, 10, 9, 5, 6]) == [9, 5, 6]
    assert sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert sol.findDuplicates([1, 1, 2, 2]) == [1, 2]
    assert sol.findDuplicates([1, 1, 2]) == [1]
    assert sol.findDuplicates([1, 2]) == []
