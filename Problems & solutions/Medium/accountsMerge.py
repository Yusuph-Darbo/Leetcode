# Approach:
# Map each email to a unique index and build a graph connecting emails
# belonging to the same account. Use BFS to find connected email groups,
# then sort each group and attach it to the account name.
#
# Time: O((n∗m)log(n∗m))
# Space: O(n∗m)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        # Email -> id
        emailIdx = {}
        # Set of emails to all accounts
        emails = []
        # Email id -> account id
        emailToAcc = {}

        m = 0
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailToAcc[m] = accId
                m += 1

        adj = [[] for _ in range(m)]

        for a in accounts:
            for i in range(2, len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        # index of acc -> list of emails
        emailGroup = defaultdict(list)

        seen = [False] * m

        def bfs(start, accId):
            queue = deque([start])
            seen[start] = True
            while queue:
                node = queue.popleft()
                emailGroup[accId].append(emails[node])
                for nei in adj[node]:
                    if not seen[nei]:
                        seen[nei] = True
                        queue.append(nei)

        for i in range(m):
            if not seen[i]:
                bfs(i, emailToAcc[i])

        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))

        return res
