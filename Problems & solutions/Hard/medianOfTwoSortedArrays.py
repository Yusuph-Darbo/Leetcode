# Approach:
# Perform binary search on the smaller array to find a partition
# where all elements on the left side are less than or equal to
# all elements on the right side. Use the partition to compute
# the median based on whether the total length is odd or even.
#
# Time: O(log(min(m, n)))
# Space: O(1)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True:
            # A
            i = l + (r - l) // 2
            # B
            j = half - i - 2

            Aleft = a[i] if i >= 0 else float("-inf")
            Aright = a[i + 1] if (i + 1) < len(a) else float("inf")
            Bleft = b[j] if j >= 0 else float("-inf")
            Bright = b[j + 1] if (j + 1) < len(b) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
