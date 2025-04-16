class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        JewelSet = set(jewels)
        return sum(stone in JewelSet for stone in stones)
        