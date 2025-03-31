class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        dp[n - 1][m - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]  

        return dp[0][0]