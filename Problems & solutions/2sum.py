# Approach:
# Iterate through the list while storing seen numbers in a hashmap (value → index).
# For each number, compute the complement (target - value).
# If the complement has already been seen, return the stored index and current index.
#
# Time Complexity: O(n) — we visit each element once and hashmap lookups are O(1) on average.
# Space Complexity: O(n) — we may store up to n elements in the hashmap.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {} # index : value

        # Turns the list in a hashmap
        for index, value in enumerate(nums):
            diff = target - value
            if diff in table:
                return[table[diff], index]
            table[value] = index

        return []
