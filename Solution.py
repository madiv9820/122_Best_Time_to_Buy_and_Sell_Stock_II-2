from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: No prices? No profit. Simple as that. 🙃
        if len(prices) == 0: return 0  

        # Initial conditions:
        # cash = Maximum profit when NOT holding a stock. (We start with cash in hand.) 💸
        # hold = Maximum profit when holding a stock. (We bought the first stock at the beginning.) 🛒
        cash, hold = 0, -prices[0]  

        # Iterate through the price list starting from the second day.
        for price in prices[1:]:
            # Option 1: We don’t hold any stock today, so either:
            # 1️⃣ Keep the cash we had before OR
            # 2️⃣ Sell the stock we were holding (profit = hold + current price).
            cash = max(cash, hold + price)  

            # Option 2: We hold a stock today, so either:
            # 1️⃣ Keep holding the same stock OR
            # 2️⃣ Buy a new stock using the cash we have (profit = cash - current price).
            hold = max(hold, cash - price)  

        # Final profit is the maximum cash we can have without holding any stock. 🏆
        return cash