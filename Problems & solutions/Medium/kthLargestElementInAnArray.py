# Approach:
# Maintain a min heap of size k while iterating through the array.
# If the heap grows larger than k, remove the smallest element.
# After processing all numbers, the heap root is the k-th largest element.
#
# Time: O(n log k)
# Space: O(k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
