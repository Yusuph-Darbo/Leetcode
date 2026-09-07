# Approach:
# Iterate through each word and add its index if it contains the target
# character.
#
# Time: O(n * m)
# Space: O(n)


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        found = []

        for i, word in enumerate(words):
            if x in word:
                found.append(i)

        return found
