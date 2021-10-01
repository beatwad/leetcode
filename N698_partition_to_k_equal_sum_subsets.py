class Solution:
    def canPartitionKSubsets(self, nums: list, k: int) -> bool:
        if len(nums) < k or int(sum(nums) / k) != sum(nums) / k:
            return False
        nums.sort(reverse=True)
        parts = [sum(nums) / k] * k

        def dfs(nums, parts, idx):
            if idx == len(nums):
                return not sum(parts)
            for i in range(len(parts)):
                if parts[i] >= nums[idx]:
                    parts[i] -= nums[idx]
                    if dfs(nums, parts, idx+1):
                        return True
                    parts[i] += nums[idx]
            return False

        return dfs(nums, parts, 0)


if __name__ == '__main__':
    sol = Solution()
    assert (sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True)
    assert (sol.canPartitionKSubsets([1, 2, 3, 4], 3) is False)
    assert (sol.canPartitionKSubsets([1, 1, 1, 1], 4) is True)
    assert (sol.canPartitionKSubsets([1, 2, 1, 1], 4) is False)
    assert (sol.canPartitionKSubsets([1, 1, 1, 1, 2, 2, 4], 3) is True)
    assert (sol.canPartitionKSubsets([1], 1) is True)
    assert (sol.canPartitionKSubsets([1, 2], 2) is False)
    assert (sol.canPartitionKSubsets([1, 2, 1], 2) is True)
    assert (sol.canPartitionKSubsets([1, 2, 1], 3) is False)
    assert (sol.canPartitionKSubsets([10, 2, 1], 3) is False)
    assert (sol.canPartitionKSubsets([13, 10, 10], 3) is False)
    assert (sol.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4) is False)
    assert (sol.canPartitionKSubsets([3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871,
                                      269], 5) is True)
