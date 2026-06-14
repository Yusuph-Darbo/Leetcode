def mergeIntervals(intervals):
    # Sorting by start times
    intervals.sort(key=lambda x: x[0])
    res = []

    if not intervals:
        return []

    prev = intervals[0]

    for start, end in intervals[1:]:
        # Merge
        if start <= prev[1]:
            prev[1] = max(end, prev[1])
        # No merge
        else:
            res.append(prev)
            prev = [start, end]

    res.append(prev)

    return res


print(mergeIntervals([]))
