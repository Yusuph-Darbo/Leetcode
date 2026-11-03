# Approach:
# Build a graph mapping each bus stop to the buses that visit it.
# Use BFS starting from the source stop, exploring all stops reachable
# through each bus. Each BFS level represents taking one additional bus.
# Track visited buses and stops to avoid redundant exploration.
#
# Time: O(N + M)
# Space: O(M + B)


class Solution:
    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        graph = defaultdict(list)

        for busId, route in enumerate(routes):
            for stop in route:
                graph[stop].append(busId)

        if source not in graph or target not in graph:
            return -1

        if target == source:
            return 0

        q = deque([source])
        busesTaken = set()
        stopsVisited = set()
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                currStop = q.popleft()

                for busId in graph[currStop]:
                    # visited before
                    if busId in busesTaken:
                        continue

                    busesTaken.add(busId)

                    for nextStop in routes[busId]:
                        # visited before
                        if nextStop in stopsVisited:
                            continue

                        if nextStop == target:
                            return res

                        q.append(nextStop)
                        stopsVisited.add(nextStop)

        return -1
