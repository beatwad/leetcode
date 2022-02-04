from typing import *
from collections import Counter


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_table = {0: -1}
        count, max_len = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in hash_table:
                max_len = max(max_len, i - hash_table[count])
            else:
                hash_table[count] = i

        return max_len


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMaxLength([0]) == 0
    assert sol.findMaxLength([1]) == 0
    assert sol.findMaxLength([0, 1]) == 2
    assert sol.findMaxLength([0, 1, 0]) == 2
    assert sol.findMaxLength([0, 0, 1, 0, 0]) == 2
    assert sol.findMaxLength([1, 0, 0, 1, 0, 0]) == 4
    assert sol.findMaxLength([0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]) == 14
