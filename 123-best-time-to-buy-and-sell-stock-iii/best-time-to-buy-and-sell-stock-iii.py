class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def f(i, buy, cap):
            profit = 0
            if i == n:
                return 0
            if cap == 0:
                return 0
            if (i, buy, cap) in dp:
                return dp[(i, buy, cap)]

            if buy:
                profit = max(-prices[i] + f(i + 1, 0, cap), 0 + f(i + 1, 1, cap))
            else:
                profit = max(prices[i] + f(i + 1, 1, cap - 1), 0 + f(i + 1, 0, cap))
            
            dp[(i, buy, cap)] = profit
            return profit

        return f(0, 1, 2)