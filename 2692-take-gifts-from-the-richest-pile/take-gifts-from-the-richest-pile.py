class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)

        while k > 0:
            gift = abs(heapq.heappop(gifts))
            heapq.heappush(gifts, -(math.floor(math.sqrt(gift))))
            k -= 1

        return abs(sum(gifts))
