# Approach:
# Sort the asteroids by size and process them from smallest
# to largest. Absorb an asteroid if the current mass is large
# enough, increasing the mass; otherwise, return False.
#
# Time: O(n log n)
# Space: O(1)


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for num in asteroids:
            if mass >= num:
                mass += num
            else:
                return False

        return True
