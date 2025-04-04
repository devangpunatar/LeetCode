class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left part of the data stream
        self.min_heap = [] # right part of the data stream

    def addNum(self, num: int) -> None:
        # Always push to max_heap first (as -num to simulate max-heap)
        heapq.heappush(self.max_heap, -num) 

        # Balance step: move the largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Fix size imbalance (if min_heap is bigger, move one back to max_heap)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            x = -self.max_heap[0]
            y = self.min_heap[0]
            return (x + y) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()