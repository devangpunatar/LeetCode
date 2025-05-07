import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        
        # Initialize the heap with at most k elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)  # Keep only k largest elements
        return self.minheap[0]  # k-th largest is the smallest in the heap
