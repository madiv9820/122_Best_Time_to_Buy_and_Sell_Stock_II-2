from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalDays = len(prices)  # Total number of days we're playing the stock market game. 🎲

        # Memoization table to store the maximum profit from each day to avoid redundant calculations. 
        # It's like having a cheat sheet for the stock market. 📋
        max_Profit_From_Ith_Day = [-1] * (totalDays + 1)  

        # Recursive function to find the maximum profit starting from a given day.
        def find_Max_Profit_From_Ith_Day(currentDay: int, buyDay: int) -> int:
            # Base case: If we've gone past the last day, it's game over. 🎯
            if currentDay > totalDays:
                return -1000000  # Return a sad number because no one likes a losing streak. 😢
            
            # Check if we've already calculated the max profit for the current day. 
            # This is the memoization part—no need to redo the same work twice. 🔄
            if max_Profit_From_Ith_Day[currentDay] == -1:
                # If we haven't decided when to buy yet, set the buy day to the current day. 🤔
                if buyDay == -1:
                    buyDay = currentDay  # First chance to buy—let’s not miss it! 🛒

                maxProfit_From_Current_Day = 0  # Starting with zero profit because we're optimistic… for now. 😅

                # Loop through all the days from the current day to the last day.
                for day in range(currentDay, totalDays):
                    # Calculate the profit if we sell on this day after buying on the buyDay. 💸
                    sell_the_Stock = prices[day] - prices[buyDay]  

                    # Calculate the profit if we hold on to the stock (i.e., skip selling today). 
                    # Because patience is key, right? 🙃
                    hold_the_Stock = find_Max_Profit_From_Ith_Day(day + 1, -1)  

                    # Decide whether to sell today or keep holding.  
                    # We're basically saying: "Do I want to be rich today or tomorrow?"  
                    maxProfit_From_Current_Day = max(maxProfit_From_Current_Day, sell_the_Stock + hold_the_Stock)
                
                # Store the calculated maximum profit for the current day to avoid redundant work later. 🗃️
                max_Profit_From_Ith_Day[currentDay] = maxProfit_From_Current_Day

            # Return the cached maximum profit for the current day (memoization at work!). 🧠
            return max_Profit_From_Ith_Day[currentDay]

        # Start the recursive journey from day 0 with no buy day set yet.  
        return find_Max_Profit_From_Ith_Day(0, -1)