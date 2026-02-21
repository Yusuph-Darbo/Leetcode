# Approach:
# Use Counter to count the frequency of each character in magazine.
#
# Iterate through each character in ransomNote:
# - If the character is not in the Counter, return False because
#   magazine does not have enough of that character.
#
# - If the character exists, decrease its count in the Counter.
#
# - If the count becomes zero, remove the character from the Counter
#   to indicate no more occurrences are available.
#
# If all characters in ransomNote are successfully matched,
# return True.
#
# Time Complexity: O(n + m) — where n is length of ransomNote and m is length of magazine.
# Space Complexity: O(1) — extra space is constant since alphabet size is limited.


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        counter = Counter(magazine)

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        
        return True
        