class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left part of the data stream
        self.min_heap = [] # right part of the data stream
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        # before I add elements to the left part, check multiple conditions:
        # check if the number of elements in the right part is equal or 1 greater
        # if the num value is greater than than the max of left part

        # Always push to max_heap first (as -num to simulate max-heap)
        heapq.heappush(self.max_heap, -num) 

        # Balance step: move the largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))


        # Fix size imbalance (if min_heap is bigger, move one back to max_heap)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        '''    
        elif (-num <= -self.max_heap[0]) and (len(self.max_heap) == len(self.min_heap) + 1):
            heapq.heappush(self.min_heap, num)

        elif (-num <= -self.max_heap[0]) and (len(self.max_heap) == len(self.min_heap) ):
            heapq.heappush(self.min_heap, num)
        elif (-num >= -self.max_heap[0]) and (len(self.max_heap) == len(self.min_heap) ):
            heapq.heappush(self.max_heap, -num)

        elif (-num >= -self.max_heap[0]) and (len(self.max_heap) == len(self.min_heap) + 1):
            heapq.heappush(self.max_heap, -num)
            x = abs(heapq.heappop(self.max_heap))
            heapq.heappush(self.min_heap, x)

        elif (-num <= -self.max_heap[0]) and (len(self.min_heap) == len(self.max_heap) + 1):
            heapq.heappush(self.min_heap, num)
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        '''
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) == len(self.max_heap):
            x = -self.max_heap[0]
            y = self.min_heap[0]

            return (x + y) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()