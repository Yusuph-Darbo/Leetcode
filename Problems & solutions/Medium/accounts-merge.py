# Approach:
# Map each email to a unique index and build a graph connecting emails
# belonging to the same account. Use BFS to find connected email groups,
# then sort each group and attach it to the account name.
#
# Time: O((n∗m)log(n∗m))
# Space: O(n∗m)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        graph = defaultdict(list)
        res = []

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                emailToName[email] = name

            first = account[1]

            for email in account[2:]:
                graph[first].append(email)
                graph[email].append(first)

        seen = set()

        def bfs(start):
            q = deque([start])
            seen.add(start)
            comp = []

            while q:
                email = q.popleft()
                comp.append(email)

                for nei in graph[email]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)

            return comp

        for email in emailToName:
            if email not in seen:
                emails = bfs(email)
                res.append([emailToName[email]] + sorted(emails))

        return res
