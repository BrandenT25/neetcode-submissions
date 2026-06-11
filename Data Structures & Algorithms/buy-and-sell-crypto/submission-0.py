class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100000
        current_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > current_profit:
                current_profit = profit
        return current_profit