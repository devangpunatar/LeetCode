class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic Programming Solution
        n = len(s)
        if not s or s[0] == "0":
            return 0
            
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # One-digit check
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two-digit check
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

        '''
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
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            cache[i] = res
            return res

        return dfs(0)

        '''
