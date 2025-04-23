class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        minHeap = [[0, 0, 0]] # [diff, r, c]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue

            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in directions:
                newR, newC = r + dr, c + dc 
                if (newR < 0 or newR == rows or newC < 0 or newC == cols or (newR, newC) in visited):
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])
        return
