# Approach:
# Use a sliding window with a hashmap to track fruit counts. Expand the
# window while there are at most two fruit types, and shrink it from the
# left when a third type is added. Track the largest valid window.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapp = {}
        l = 0
        res = 0

        for r in range(len(fruits)):
            mapp[fruits[r]] = 1 + mapp.get(fruits[r], 0)

            while len(mapp) > 2:
                mapp[fruits[l]] -= 1

                if mapp[fruits[l]] == 0:
                    del mapp[fruits[l]]

                l += 1

            res = max(res, (r - l + 1))

        print(mapp)

        return res
