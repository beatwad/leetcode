class Solution:
    def singleNumber(self, nums: list) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


if __name__ == '__main__':
    sol = Solution()
    assert sol.singleNumber([1, 2, 1, 2, 4]) == 4
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([1, 2, 1]) == 2
    assert sol.singleNumber([1, 2, 1, 2, 3, 3, 5, 7, 4, 5, 4]) == 7
