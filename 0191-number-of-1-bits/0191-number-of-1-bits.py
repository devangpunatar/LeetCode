class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = str(bin(n)[2:])
        count = 0
        for c in temp:
            if c == '1':
                count += 1
        return count