from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)  # Total number of days we're trading in the stock market. 🎯

        # Edge case: No prices? No profit. Simple math. 🙃
        if totalDays == 0: return 0  

        # DP table to track two states for each day:
        # [0] => Max profit when we don't hold a stock (i.e., cash in hand). 💰
        # [1] => Max profit when we hold a stock. 🛒
        cash_And_Hold_At_Ith_Day = [[0] * 2 for _ in range(totalDays)]  

        # Day 0: We either have no stock (cash) or we bought one on day 0.
        cash_And_Hold_At_Ith_Day[0][0] = 0              # Starting with $0 in cash. 💸
        cash_And_Hold_At_Ith_Day[0][1] = -prices[0]      # Bought the stock on day 0, so we’re already in the red. 😬

        # DP transitions for each day from day 1 onwards.
        for currentDay in range(1, totalDays):
            # If we don’t hold a stock today, we either:
            # 1️⃣ Keep the cash from the previous day OR
            # 2️⃣ Sell the stock we were holding.
            cash_And_Hold_At_Ith_Day[currentDay][0] = max(
                cash_And_Hold_At_Ith_Day[currentDay - 1][0],  # Keep the cash from the previous day. 💼
                cash_And_Hold_At_Ith_Day[currentDay - 1][1] + prices[currentDay]  # Sell today’s stock. 📈
            )

            # If we hold a stock today, we either:
            # 1️⃣ Keep holding the stock from the previous day OR
            # 2️⃣ Buy a new stock with the cash we have.
            cash_And_Hold_At_Ith_Day[currentDay][1] = max(
                cash_And_Hold_At_Ith_Day[currentDay - 1][1],  # Hold the same stock. 🤝
                cash_And_Hold_At_Ith_Day[currentDay - 1][0] - prices[currentDay]  # Buy a new stock. 🛒
            )

        # The answer is the max profit we can have on the last day without holding any stock. 🏆
        return cash_And_Hold_At_Ith_Day[totalDays - 1][0]