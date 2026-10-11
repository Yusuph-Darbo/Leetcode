# Approach:
# Store all starting cities in a set. The destination city is the one that
# never appears as a starting city.
#
# Time: O(n)
# Space: O(n)


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = set()

        for path in paths:
            cities.add(path[0])

        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest

        return ""
