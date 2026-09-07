# Approach:
# Traverse the array twice, appending each element to the result to create
# two consecutive copies of the original array.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            ans.append(num)

        for num in nums:
            ans.append(num)

        return ans
