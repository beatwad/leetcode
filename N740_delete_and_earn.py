from typing import *
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        total_sum = 0
        for k, v in num_counter.items():
            total_sum += k*v

        def max_points(x):
            gain = 0
            return max(max_points(x-1), max_points(x-2) + gain)

        def helper(total_sum, num_counter):
            best_key, max_sum = None, 0
            for k, v in num_counter.items():
                num_sum = total_sum - k * v
                if k-1 in num_counter: num_sum -= (k-1) * num_counter[k-1]
                if k+1 in num_counter: num_sum -= (k+1) * num_counter[k+1]
                if k*v + num_sum > max_sum:
                    max_sum = k*v + num_sum
                    best_key = k
            return best_key, best_key * num_counter[best_key]

        res = 0
        while num_counter:
            best_key, max_sum = helper(total_sum, num_counter)
            res += max_sum
            total_sum -= max_sum
            del num_counter[best_key]
            if best_key-1 in num_counter: del num_counter[best_key-1]
            if best_key+1 in num_counter: del num_counter[best_key+1]

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.deleteAndEarn([3, 4, 2]) == 6
    assert sol.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
