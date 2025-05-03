class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        minHeap = []
        res = 0
        for meetings in intervals:
            while minHeap and minHeap[0] <= meetings[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, meetings[1])
            res = max(res, len(minHeap))
        
        return res
