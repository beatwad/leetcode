from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        nums3 = []
        while i < m or j < n:
            if i == m:
                nums3.extend(nums2[j:n])
                j = n
            elif j == n:
                nums3.extend(nums1[i:m])
                i = m
            elif nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        nums1[:] = nums3


if __name__ == '__main__':
    sol = Solution()
    nums1, nums2 = [1, 2, 3, 4, 5, 6, 0, 0, 0], [2, 5, 6]
    sol.merge(nums1, 6, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 4, 5, 5, 6, 6]

    nums1, nums2 = [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 6]
    sol.merge(nums1, 6, nums2, 6)
    assert nums1 == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1, nums2 = [1], []
    sol.merge(nums1, 1, nums2, 0)
    assert nums1 == [1]

    nums1, nums2 = [], [1]
    sol.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]

    nums1, nums2 = [1], [1]
    sol.merge(nums1, 0, nums2, 0)
    assert nums1 == []

    nums1, nums2 = [1], [1]
    sol.merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 1]

    nums1, nums2 = [0], [1]
    sol.merge(nums1, 0, nums2, 1)
    assert nums1 == [1]

    nums1, nums2 = [], []
    sol.merge(nums1, 0, nums2, 0)
    assert nums1 == []
