class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                res += 1
                if end > intervals[i][1]:
                    start, end = intervals[i][0], intervals[i][1]
                elif end <= intervals[i][1]:
                    continue
            else:
                start, end = intervals[i][0], intervals[i][1]

        return res