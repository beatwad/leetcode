class Solution:
    def permute(self, nums: list) -> list:
        ans = []
        n = len(nums)

        def helper(nums, res):
            if len(res) == n:
                ans.append(res)
            for i, v in enumerate(nums):
                helper(nums[:i] + nums[i+1:], res + [v])

        helper(nums, [])
        return ans


if __name__ == '__main__':
    sol = Solution()
    assert sol.permute([1]) == [[1]]
    assert sol.permute([0, 1]) == [[0, 1], [1, 0]]
    assert sol.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
