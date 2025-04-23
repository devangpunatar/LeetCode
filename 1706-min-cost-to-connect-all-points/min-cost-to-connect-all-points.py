class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [[0, 0]] # [cost, point_idx]
        n = len(points)
        visited = set()
        totalCost = 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            visited.add(i)
            totalCost += cost

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    xi, yi = points[i]
                    dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, [dist, j])

        return totalCost