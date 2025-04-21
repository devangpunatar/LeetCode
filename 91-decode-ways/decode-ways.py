class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0

            else:
                dp[i] = dp[i + 1]
                
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]


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
