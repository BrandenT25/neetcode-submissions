class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10000
        topProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            currentProfit = price - minPrice
            if currentProfit > topProfit:
                topProfit = currentProfit
        return topProfit
