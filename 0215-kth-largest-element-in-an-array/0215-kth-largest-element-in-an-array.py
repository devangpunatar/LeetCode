class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n_nums = [-n for n in nums]
        heapq.heapify(n_nums)

        while k > 1:
            heapq.heappop(n_nums)
            k -= 1
        
        return -heapq.heappop(n_nums)


