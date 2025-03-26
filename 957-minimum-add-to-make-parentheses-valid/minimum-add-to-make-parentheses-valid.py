class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openP, closeP = 0, 0

        for c in s:
            if c == "(":
                openP += 1
            elif c == ")" and openP >= 1:
                openP -= 1
            elif c == ")" and openP == 0:
                closeP += 1

        return openP + closeP
