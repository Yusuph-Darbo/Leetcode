# Approach:
# Use backtracking to build valid parentheses strings. Add an opening
# parenthesis while possible, and only add a closing parenthesis when there
# are more opening than closing parentheses.
#
# Time: Exponential
# Space: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def backtrack(l , r):
            if l == r == n:
                res.append(''.join(path))
                return

            if l < n:
                path.append('(')
                backtrack(l + 1, r)
                path.pop()

            if r < l:
                path.append(')')
                backtrack(l, r + 1)
                path.pop()

        backtrack(0, 0)

        return res