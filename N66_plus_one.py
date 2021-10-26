class Solution:
    def plusOne(self, digits: list) -> list:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        else:
            digits = [1] + digits
        return digits


if __name__ == '__main__':
    sol = Solution()
    assert sol.plusOne([0]) == [1]
    assert sol.plusOne([9]) == [1, 0]
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert sol.plusOne([9, 9, 9, 8]) == [9, 9, 9, 9]
    assert sol.plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]

