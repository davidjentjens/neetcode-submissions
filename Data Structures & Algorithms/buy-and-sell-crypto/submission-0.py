class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = float('inf')
        profit = 0
        for price in prices:
            lowest_buy_price = min(price, lowest_buy_price)
            profit = max(profit, price - lowest_buy_price)
        return profit