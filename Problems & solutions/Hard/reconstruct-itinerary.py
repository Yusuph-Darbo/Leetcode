# Approach:
# Use Hierholzer's algorithm (DFS) to construct an Eulerian path.
# Sort destinations in reverse lexicographical order so popping from the
# end always selects the smallest available destination.
# Append each airport after exploring all its outgoing tickets, then
# reverse the result to obtain the itinerary.
#
# Time: O(E log E), where E is the number of tickets
# Space: O(E) for the graph and result


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        tickets.sort(reverse=True)

        for v, e in tickets:
            graph[v].append(e)

        res = []

        def dfs(src):
            while graph[src]:
                nei = graph[src].pop()
                dfs(nei)

            res.append(src)

        dfs("JFK")

        return res[::-1]
