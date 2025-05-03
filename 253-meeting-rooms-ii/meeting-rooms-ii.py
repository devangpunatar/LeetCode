import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Use a min-heap to track end times of meetings
        min_heap = []  # stores end times

        for meeting in intervals:
            start, end = meeting

            # If the earliest ending meeting is done, reuse that room
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Allocate the current meeting's end time
            heapq.heappush(min_heap, end)

        # Step 3: The heap size is the number of rooms needed
        return len(min_heap)
