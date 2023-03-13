from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))

        if len(nums) == 1:
            if nums[0] == target:
                return True
            return False

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return True
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.search([1], 1) is True
    assert sol.search([1], 0) is False
    assert sol.search([0, 0], 0) is True
    assert sol.search([1, 1], 0) is False
    assert sol.search([0, 0, 0], 0) is True
    assert sol.search([2, 0, 1, 2], 1) is True
    assert sol.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert sol.search([2, 5, 6, 6, 0, 0, 1, 2], 8) is False
    assert sol.search([2, 5, 6, 6, 6, 6, 0, 0, 1, 2], 8) is False
    assert sol.search([0, 0, 0, 0, 0, 0, 0, 0], 0) is True
    assert sol.search([0, 0, 0, 0, 0, 0, 0, 0], 8) is False
    assert sol.search([6, 6, 6, 6, 0, 0, 1, 2], 8) is False
    assert sol.search([6, 6, 6, 6, 0, 0, 1, 2], 6) is True
    assert sol.search([6, 0, 0, 1, 2, 3, 4, 4, 4, 5], 6) is True
    assert sol.search([6, 1, 2, 3, 4, 5], -10) is False
    assert sol.search([6, 1, 2, 3, 4, 5], 6) is True
    assert sol.search([6, 0, 0, 1, 2, 3, 4, 4, 4, 5], -10) is False
    assert sol.search([6, -10, 0, 1, 2, 3, 4, 4, 4, 5], -10) is True
    assert sol.search([6, -10, 0, 1, 2, 3, 4, 4, 4, 5], 3) is True
    assert sol.search([-10, 0, 1, 2, 3, 4, 4, 4, 5, -20], 0) is True
    assert sol.search([-10, 0, 1, 2, 3, 4, 4, 4, 5, -20], 10) is False
    assert sol.search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2) is True


    def rle_encode(st):
        res = ''
        cnt = 0
        prev = st[0]
        for i in range(len(st)):
            if st[i] != prev:
                res += str(cnt) + st[i-1]
                cnt = 1
                prev = st[i]
            else:
                cnt += 1

        res += str(cnt) + prev
        return res

    print(rle_encode('F'))
    assert rle_encode('ABCABCABCDDDFFFFFF') == '1A1B1C1A1B1C1A1B1C3D6F'