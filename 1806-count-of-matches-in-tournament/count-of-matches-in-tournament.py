class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2 == 0:
                res += (n // 2)
                n = n // 2
            elif n % 2 == 1:
                res += (n - 1) // 2
                n = (n // 2) + 1
            
        return res
