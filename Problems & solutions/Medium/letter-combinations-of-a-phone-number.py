# Approach:
# Use iterative backtracking to build all possible letter combinations.
# Start with an empty string and, for each digit, append every corresponding
# letter to each existing combination. Repeat until all digits are processed.
#
# Time: O(n ∗ 4^n)
# Space: O(n * 4^n)


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for d in digits:
            temp = []
            for curStr in res:
                for c in digitToChar[d]:
                    temp.append(curStr + c)

            res = temp

        return res
