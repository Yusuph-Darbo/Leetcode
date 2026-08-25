# Approach:
# Merge the arrays from right to left, placing the larger element at the
# end of nums1. This avoids overwriting elements that still need to be used.
#
# Time: O(m + n)
# Space: O(1)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = n - 1
        k = m - 1

        while j >= 0:
            if k >= 0 and nums1[k] > nums2[j]:
                nums1[i] = nums1[k]
                k -= 1
            else:
                nums1[i] = nums2[j]
                j -= 1
            i -= 1
