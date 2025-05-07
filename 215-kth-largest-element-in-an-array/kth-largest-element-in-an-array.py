class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-n for n in nums]
        heapq.heapify(minHeap)
        for _ in range(k):
            res = heapq.heappop(minHeap)
        return -res