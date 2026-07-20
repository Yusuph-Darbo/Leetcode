# Approach:
# Create a mapping from each alien character to its position in the custom
# alphabet. Compare each adjacent pair of words character by character,
# ensuring they appear in the correct lexicographical order according to
# the alien language rules.
#
# Time: O(n * m)
# Space: O(1)


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[1 + i]

            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True
