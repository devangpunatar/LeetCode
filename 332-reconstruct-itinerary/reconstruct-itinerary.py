from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Step 1: Build min-heap for each airport's destinations
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)

        result = []

        # Step 2: DFS function
        def dfs(airport):
            # Visit all destinations in lexical order
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            result.append(airport)

        # Step 3: Start DFS from JFK
        dfs("JFK")
        return result[::-1]  # reverse to get correct order
