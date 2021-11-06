class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        xor = xor & (xor - 1) ^ xor
        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    sol = Solution()
    assert sol.singleNumber([1, 5, 2, 5, 1, 0]) == [2, 0]
    assert sol.singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5]
