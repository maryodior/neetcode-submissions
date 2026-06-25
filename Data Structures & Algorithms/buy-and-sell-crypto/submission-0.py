from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max_profit to 0 (covers the case where no profit can be made)
        max_profit = 0
        # Start by assuming the first day is the lowest price
        min_price = prices[0]
        
        for price in prices:
            # If we find a lower price, update our buying point
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a better profit
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    
        return max_profit