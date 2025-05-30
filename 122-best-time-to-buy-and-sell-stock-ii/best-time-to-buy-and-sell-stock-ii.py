class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ahead = [0, 0]  # represents dp[i + 1]
        curr = [0, 0]   # represents dp[i]

        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                if buy:
                    curr[buy] = max(-prices[i] + ahead[0],
                                    ahead[1])
                else:
                    curr[buy] = max(prices[i] + ahead[1],
                                    ahead[0])
            ahead = curr[:]

        return ahead[1]


'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][buy] → max profit from day i with 'buy' permission
        dp = [[0] * 2 for _ in range(n + 1)]
        
        # start filling dp from the end of days
        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                if buy:
                    dp[i][buy] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
                else:
                    dp[i][buy] = max(prices[i] + dp[i + 1][1], 0 + dp[i + 1][0])

        return dp[0][1]
'''