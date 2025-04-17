class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        result = {}
        res = 0
        for u, v, w in times:
            adjList[u].append([v, w])

        minHeap = [[0, k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in result:
                continue
            
            result[n1] = w1
            res = max(res, w1)
            if len(result) == n:
                return res

            for n2, w2 in adjList[n1]:
                if n2 not in result:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        return -1