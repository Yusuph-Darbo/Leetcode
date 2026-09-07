# Approach:
# Build a prefix sum array where each index represents the cumulative weight.
# To pick an index, generate a random number between 1 and the total weight,
# then use binary search to find the first prefix sum greater than or equal
# to that number. This ensures each index is selected with probability
# proportional to its weight.
#
# Time: O(n) for initialization, O(log n) per pickIndex call
# Space: O(n)


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0

        for num in w:
            total += num
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        num = random.randint(1, self.total)

        l, r = 0, len(self.prefix) - 1

        while l < r:
            mid = l + (r - l) // 2

            if self.prefix[mid] >= num:
                r = mid
            else:
                l = mid + 1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
