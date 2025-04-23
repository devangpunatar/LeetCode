class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for u, v, w in flights:
            adjList[u].append([v, w])

        res = float('inf')
        best = {}
        minHeap = [[0, src, 0]] # [price, nodeIndx, stops]

        while minHeap:
            price, i, stops = heapq.heappop(minHeap)
            
            if i == dst:
                return price

            if stops > k:
                continue

            for v, w in adjList[i]:
                if (v, stops + 1) not in best or price + w < best[(v, stops + 1)]:
                    best[(v, stops + 1)] = price + w
                    heapq.heappush(minHeap, [price + w, v, stops + 1])

        return -1