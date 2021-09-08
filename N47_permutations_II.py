class Solution:
    def permuteUnique(self, nums: list) -> list:
        ans = list()
        n = len(nums)
        nums.sort()

        def helper(nums, res):
            if len(res) == n:
                ans.append(res)
            for i, v in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                helper(nums[:i] + nums[i+1:], res + [v])

        helper(nums, [])
        return list(ans)


if __name__ == '__main__':
    sol = Solution()
    assert sol.permuteUnique([1]) == [[1]]
    assert sol.permuteUnique([0, 1]) == [[0, 1], [1, 0]]
    assert sol.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert sol.permuteUnique([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
