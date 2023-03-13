from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()

        def helper(comb, nums):
            if comb not in res:
                res.append(comb)
            for i in range(len(nums)):
                helper(comb + [nums[i]], nums[i+1:])

        helper([], nums)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.subsetsWithDup([1]) == [[], [1]]
    assert sol.subsetsWithDup([1, 2]) == [[], [1], [1, 2], [2]]
    assert sol.subsetsWithDup([1, 2, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]


