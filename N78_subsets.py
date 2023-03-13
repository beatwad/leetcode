from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, comb):
            res.append(comb)
            for i in range(len(nums)):
                backtrack(nums[i+1:], comb + [nums[i]])

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.subsets([1]) == [[], [1]]
    assert sol.subsets([1, 2]) == [[], [1], [1, 2], [2]]
    assert sol.subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
