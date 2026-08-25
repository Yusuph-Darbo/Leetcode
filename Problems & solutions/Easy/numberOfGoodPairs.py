# Approach:
# Use a hashmap to count previous occurrences of each number. Each time a
# number appears, it forms a new pair with every previous occurrence.
#
# Time: O(n)
# Space: O(n)


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = 0

        table = defaultdict(int)

        for n in nums:
            # If number is already seen, it can form pairs with all previous occurrences
            if n in table:
                count += table[n]
                table[n] += 1

            else:
                table[n] = 1

        return count
