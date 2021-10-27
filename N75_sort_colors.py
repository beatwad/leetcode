class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
    nums = [0]
    sol.sortColors(nums)
    assert nums == [0]
    nums = [1]
    sol.sortColors(nums)
    assert nums == [1]
    nums = [2, 0, 1]
    sol.sortColors(nums)
    assert nums == [0, 1, 2]
