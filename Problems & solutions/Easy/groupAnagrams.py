# Approach:
# Use a dictionary to group words that are anagrams of each other.
# The key idea is that anagrams have the same character frequency.
#
# For each word, create a count array of size 26 to store the frequency
# of each letter from 'a' to 'z'.
#
# Convert this count array into a tuple so it can be used as a dictionary key.
#
# Use this tuple as the key and append the word to the corresponding list.
#
# After processing all words, each dictionary value will contain a group
# of anagrams.
#
# Return all the grouped anagrams.
#
# Time Complexity: O(n * k) — where n is number of words and k is average word length.
# Space Complexity: O(n * k) — space used to store the groups and keys.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            # Lists are mutable and cannot be dict keys
            table[tuple(count)].append(word)

        return table.values()