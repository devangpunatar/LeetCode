class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        n_stones = [-w for w in stones]
        heapq.heapify(n_stones)

        while len(n_stones) != 1:
            y = heapq.heappop(n_stones)
            x = heapq.heappop(n_stones)
            if x == y and len(n_stones) == 0:
                return 0
            elif x != y:
                temp = y - x
                heapq.heappush(n_stones, temp)
            else:
                continue
        
        return -heapq.heappop(n_stones)