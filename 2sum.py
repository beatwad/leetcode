class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res_dict = dict()
        for i, v in enumerate(nums):
            diff = target - v
            if diff in res_dict:
                return [res_dict[diff], i]
            res_dict[v] = i


if __name__ == '__main__':
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
    assert sol.twoSum([6, 0], 6) == [0, 1]
