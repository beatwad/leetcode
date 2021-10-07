class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        n = len(nums)
        freq_list = [0 for _ in range(n)]
        for num in nums:
            freq_list[num-1] += 1
        return [i+1 for i in range(n) if freq_list[i] == 0]


if __name__ == '__main__':
    sol = Solution()
    assert sol.findDisappearedNumbers([1, 3, 5, 4, 1]) == [2]
    assert sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert sol.findDisappearedNumbers([1, 1]) == [2]
    assert sol.findDisappearedNumbers([1, 2]) == []
    assert sol.findDisappearedNumbers([1]) == []
