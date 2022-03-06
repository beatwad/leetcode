from typing import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        nums_sum = nums.copy()
        hash_table = {0: 1}

        for i in range(n):
            if i > 0:
                nums_sum[i] += nums_sum[i-1]

            if nums_sum[i] - k in hash_table:
                res += hash_table[nums_sum[i] - k]

            if nums_sum[i] in hash_table:
                hash_table[nums_sum[i]] += 1
            else:
                hash_table[nums_sum[i]] = 1

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.subarraySum([0, 0], 0) == 3
    assert sol.subarraySum([0, 0, 0], 0) == 6
    assert sol.subarraySum([-1, 1], 0) == 1
    assert sol.subarraySum([-1, -1, 2, 0], 0) == 3
    assert sol.subarraySum([3], 3) == 1
    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1, 1, 1, 1], 3) == 2
    assert sol.subarraySum([1, 1, 1, 1, 1], 3) == 3
    assert sol.subarraySum([1, 1, 1, -3, 3], 3) == 3
    assert sol.subarraySum([1, 1, 1, -3, 3, 1, 2, 3, 5, 1, -1, -2, 3, -3, 1, -10, 10, 2, 4], 3) == 14
