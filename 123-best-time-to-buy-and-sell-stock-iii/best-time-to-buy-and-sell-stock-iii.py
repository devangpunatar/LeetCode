class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # dp[day][buy][cap]
        # buy: 1 = we can buy, 0 = we must sell next
        # cap: number of transactions remaining (max 2)

        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                for cap in range(1, 3):  # cap = 1 or 2
                    if buy:
                        # Choose to buy or skip
                        dp[i][buy][cap] = max(
                            -prices[i] + dp[i + 1][0][cap],  # Buy now
                            dp[i + 1][1][cap]                 # Skip buying
                        )
                    else:
                        # Choose to sell or skip
                        dp[i][buy][cap] = max(
                            prices[i] + dp[i + 1][1][cap - 1],  # Sell now
                            dp[i + 1][0][cap]                   # Skip selling
                        )

        return dp[0][1][2]  # start at day 0, allowed to buy, 2 transactions left


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