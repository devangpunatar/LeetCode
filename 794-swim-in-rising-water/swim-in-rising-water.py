class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        minHeap = [[grid[0][0], 0, 0]] # [elevation, r, c]
        res = 0
        while minHeap:
            elevation, r, c = heapq.heappop(minHeap)
            res = max(res, elevation)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return res

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newR == rows or newC < 0 or newC == cols or (newR, newC) in visited):
                    continue
                maxElev = max(elevation, grid[newR][newC])
                heapq.heappush(minHeap, [maxElev, newR, newC])

        return


