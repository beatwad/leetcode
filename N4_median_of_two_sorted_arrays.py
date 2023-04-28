class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.fm(nums1, nums2, l // 2)
        else:
            return (self.fm(nums1, nums2, l // 2) + self.fm(nums1, nums2, l // 2 - 1)) / 2

    def fm(self, nums1, nums2, mi3) -> float:
        """ Main idea:
            - if median of joined list (m3) is lesser than sum of indices of medians of two arrays (mi1 and mi2),
            than median is not in bigger part of at least one array. And this array has bigger median value
            than another. So we drop bigger part of this array
            - if index of median of joined list is bigger than sum of indices medians of two arrays,
            than median is not in lesser part of at least one array. And this array has lesser median value
            than another. So we drop lesser part of this array and also decrease median index value on mi1+1 or mi2+1
            (depends on which array has lesser median)
            - than we recursively search median in changed arrays
             """
        if not nums1:
            return nums2[mi3]
        if not nums2:
            return nums1[mi3]

        mi1 = len(nums1) // 2
        mv1 = nums1[mi1]
        mi2 = len(nums2) // 2
        mv2 = nums2[mi2]

        if mi1 + mi2 < mi3:
            if mv1 < mv2:
                return self.fm(nums1[mi1+1:], nums2, mi3 - mi1 - 1)
            else:
                return self.fm(nums1, nums2[mi2+1:], mi3 - mi2 - 1)
        else:
            if mv1 > mv2:
                return self.fm(nums1[:mi1], nums2, mi3)
            else:
                return self.fm(nums1, nums2[:mi2], mi3)


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([1], []) == 1
    assert sol.findMedianSortedArrays([], [2]) == 2
    assert sol.findMedianSortedArrays([], [2, 3]) == 2.5
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([1, 2, 3], [3, 4, 5, 6]) == 3
    assert sol.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [1, 2, 3]) == 3

