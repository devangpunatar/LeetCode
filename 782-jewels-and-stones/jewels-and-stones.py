class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        hashMap = {}
        res = 0
        for i in jewels:
            hashMap[i] = hashMap.get(i, 0)
        for c in stones:
            if c in hashMap:
                res += 1
        return res