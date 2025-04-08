class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x[0])
        
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                return False
            start, end = intervals[i][0], intervals[i][1]

        return True  

        

