class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        start, end = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            if end < intervals[i][0] and res and start > res[-1][1]:
                res.append([start, end])
            elif end < intervals[i][0] and not res:
                res.append([start, end])
            if start > intervals[i][1]:
                res.append(intervals[i])
            elif end < intervals[i][0]:
                res.append(intervals[i])
            elif start <= intervals[i][1]:
                start, end = min(intervals[i][0], start), max(intervals[i][1], end)
            elif end >= intervals[i][0]:
                start, end = min(intervals[i][0], start), max(intervals[i][1], end)

        if not res:
            res.append([start, end])
        if start > res[-1][1]:
            res.append([start, end])
        return res