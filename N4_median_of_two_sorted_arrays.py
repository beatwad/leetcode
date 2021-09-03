class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        merged_nums = self.merge(nums1, nums2)
        return self.find_median(merged_nums)[0]

    @staticmethod
    def find_median(arr):
        quot, remain = divmod(len(arr), 2)
        if remain == 0:
            return (arr[quot - 1] + arr[quot]) / 2, quot
        else:
            return arr[quot], quot

    def binary_search_median(self, arr, med):
        ind = self.find_median(arr)[1]
        if len(arr) == 1:
            return arr[0]
        if arr[ind - 1] <= med <= arr[ind]:
            return arr[ind]
        elif arr[ind] >= med:
            return self.binary_search_median(arr[:ind], med)
        else:
            return self.binary_search_median(arr[ind:], med)

    def merge(self, nums1, nums2):
        if nums1 == [] or nums2 == []:
            return nums1 + nums2
        elif nums1[-1] <= nums2[0]:
            return nums1 + nums2
        elif nums2[-1] <= nums1[0]:
            return nums2 + nums1

        med1, med_ind1 = self.find_median(nums1)
        med2, med_ind2 = self.find_median(nums2)

        if med1 == med2:
            merged_nums = self.merge(nums1[:med_ind1], nums2[:med_ind2]) + self.merge(nums1[med_ind1:],
                                                                                      nums2[med_ind2:])
            return merged_nums

        if med2 < med1:
            nums1, nums2 = nums2, nums1
            med1, med_ind1, med2, med_ind2 = med2, med_ind2, med1, med_ind1

        if nums1[-1] <= med2:
            merged_nums = self.merge(nums1, nums2[:med_ind2]) + nums2[med_ind2:]
            return merged_nums

        med_val = self.binary_search_median(nums1[med_ind1:len(nums1)], med2)
        ind = nums1.index(med_val)
        merged_nums = self.merge(nums1[:ind], nums2[:med_ind2]) + self.merge(nums1[ind:], nums2[med_ind2:])

        return merged_nums


if __name__ == '__main__':
    sol = Solution()
    assert sol.findMedianSortedArrays([1], []) == 1
    assert sol.findMedianSortedArrays([], [2]) == 2
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([0, 0], [0, 0]) == 0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert sol.findMedianSortedArrays([1, 2, 3], [3, 4, 5, 6]) == 3
    assert sol.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [1, 2, 3]) == 3

