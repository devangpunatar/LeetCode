class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
       
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        
        heap = list(count.keys())  # Get all keys
        heapq.heapify(heap)
        while heap:
            first = heap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True



        