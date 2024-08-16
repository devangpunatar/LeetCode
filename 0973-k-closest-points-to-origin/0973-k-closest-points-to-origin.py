class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        res = float('inf')

        for point in points:
            x = point[0]
            y = point[1]
            distance = (x * x) + (y * y)

            heapq.heappush(min_heap, (-distance, [x, y]))

            if len(min_heap) > k:
                heapq.heappop(min_heap) 
                
        return [point for (_, point) in min_heap]