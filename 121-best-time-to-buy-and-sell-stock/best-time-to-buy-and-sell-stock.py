class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minimum = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - minimum
            maxProfit = max(maxProfit, profit)
            minimum = min(minimum, prices[i])
            
        return maxProfit