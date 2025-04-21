class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            # Decode one digit
            res = dfs(i + 1)

            # Decode two digits if it's between 10 and 26
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            cache[i] = res
            return res

        return dfs(0)
