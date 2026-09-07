# Approach:
# Use merge sort to recursively split the array into smaller halves, then
# merge the sorted halves back together.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, low, mid, high):
            lArray = arr[low : mid + 1]
            rArray = arr[mid + 1 : high + 1]

            i = low
            j = 0
            k = 0

            while j < len(lArray) and k < len(rArray):
                if lArray[j] < rArray[k]:
                    arr[i] = lArray[j]
                    j += 1
                else:
                    arr[i] = rArray[k]
                    k += 1

                i += 1

            while j < len(lArray):
                arr[i] = lArray[j]
                j += 1
                i += 1

            while k < len(rArray):
                arr[i] = rArray[k]
                i += 1
                k += 1

        def mergeSort(arr, l, h):
            if l == h:
                return arr

            mid = l + (h - l) // 2

            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, h)
            merge(arr, l, mid, h)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
