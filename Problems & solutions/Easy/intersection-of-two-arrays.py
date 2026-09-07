# Approach:
# Sort both arrays and use two pointers to find common elements.
# When elements match, add to result (avoiding duplicates) and move both pointers;
# otherwise move the pointer of the smaller element.
#
# Time: O(n log n + m log m)
# Space: O(n) (for result storage)


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []

        nums1.sort()
        nums2.sort()

        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] not in arr:
                    arr.append(nums1[i])

                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return arr
