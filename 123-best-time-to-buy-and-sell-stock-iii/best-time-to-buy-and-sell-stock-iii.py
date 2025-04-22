class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # dp[i][buy][cap] = max profit starting at day i, buy/sell status, and cap remaining
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                for cap in range(1, 3):  # cap must be at least 1 to make a transaction
                    if buy:
                        dp[i][buy][cap] = max(-prices[i] + dp[i + 1][0][cap], 
                                              dp[i + 1][1][cap])  # buy or skip
                    else:
                        dp[i][buy][cap] = max(prices[i] + dp[i + 1][1][cap - 1], 
                                              dp[i + 1][0][cap])  # sell or skip

        return dp[0][1][2]  # start at day 0, can buy, 2 transactions left

'''
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