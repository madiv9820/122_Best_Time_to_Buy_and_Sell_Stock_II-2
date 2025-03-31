# 📈 The Stock Market Adventure! 🚀
- ### 🚨 Request for Code Review: Stock Profit Solution 🚨
    ### $\textbf{\textit{Hey there!}}$ 👋

    I've implemented a solution to the [**$\textbf{\textit{Best Time to Buy and Sell Stock II}}$**](https://github.com/madiv9820/122_Best_Time_to_Buy_and_Sell_Stock_II-2) problem. 📈💸 I’d love for you to take a look at my code and provide feedback. Whether it's a bug 🐞, an optimization suggestion ⚡, or even just a general review 🔍, all feedback is welcome!

    - ### What to Review:
        - The approach I used to solve the problem (Dynamic Programming and state transitions).
        - Code clarity and structure 🧑‍💻.
        - Any possible performance improvements or edge cases I may have missed 🧠.

    - ### How You Can Help:
        1. Check the **`maxProfit`** method in the `Solution` class.
        2. Let me know if you think there’s a better approach.
        3. Point out any code improvements (e.g., style, optimization, etc.) or test cases that are missing. 

    - ### Test Cases:
        I’ve already written some basic test cases, but I would appreciate it if you could review them and suggest additional ones, if necessary.

        Feel free to leave comments, create issues, or even submit pull requests with your suggestions. 😎

- ### Approach 1:- Recursion
    ### 🧠💰 Intuition
    Alright, so here we are, trying to make money in the stock market. The task is simple—buy low, sell high, and try not to lose your shirt. 🎲📉📈 But here’s the twist: You can buy and sell the same stock multiple times in a single day (yes, go ahead, be that person who buys coffee and sells it for a profit). The goal is to maximize your profit. 

    ### 🧐 Approach
    The approach? It's like trying to plan your life decisions... but in reverse, and with fewer regrets. The code uses **recursion** to explore all possible scenarios. It starts from a given day, and at each point, you have two choices:

    1. **Sell the stock** and count the profits. 💰
    2. **Hold onto the stock** and wait for the "perfect" moment to sell—because timing is everything. (Spoiler: It's never perfect.) 🕰️

    It does this until the last day. But oh no, there's no memoization here, so every single possibility gets recalculated. It's like a hamster running on a wheel that never gets anywhere—super efficient, right? 🐹💀

    ### ⏳ Time Complexity
    This bad boy is **$O(2^n)$**. That’s right, exponential. We’re checking every possible combination of buying and selling, and for each decision, it branches out into two choices: Sell now or hold forever. It’s like an infinite loop of regret and missed opportunities. Welcome to the stock market! 🏦🚨

    ### 🧳 Space Complexity
    A cozy **$O(n)$**. That’s the space taken up by the recursion stack. In layman’s terms, it’s like hoarding empty boxes in your attic—there’s not much there, but it still takes up space in your mind (and your code). 🏚️🧳

    ### 💻 Code Implementation
    ```python3 []
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            totalDays = len(prices)  # Total number of days we’re playing the stock market game. 🎲

            # Recursive function to find the maximum profit starting from a given day.
            def find_Max_Profit_From_Ith_Day(currentDay: int, buyDay: int) -> int:
                # Base case: If we’ve gone past the last day, it’s game over. 🎯
                if currentDay > totalDays:
                    return -1000000  # Return a sad number because no one likes a losing streak. 😢

                # If we haven’t decided when to buy yet, set the buy day to the current day. 🤔
                if buyDay == -1:
                    buyDay = currentDay  # First chance to buy—let’s not miss it!

                maxProfit_From_Current_Day = 0  # Starting with zero profit because we're optimistic… for now. 😅

                # Loop through all the days from the current day to the last day.
                for day in range(currentDay, totalDays):
                    # Calculate the profit if we sell on this day after buying on the buyDay. 💸
                    sell_the_Stock = prices[day] - prices[buyDay]  

                    # Calculate the profit if we hold on to the stock (i.e., skip selling today). 
                    hold_the_Stock = find_Max_Profit_From_Ith_Day(day + 1, -1)  # Because patience is key, right? 🙃

                    # Decide whether to sell today or keep holding.  
                    # We’re basically saying: "Do I want to be rich today or tomorrow?"  
                    maxProfit_From_Current_Day = max(maxProfit_From_Current_Day, sell_the_Stock + hold_the_Stock)

                return maxProfit_From_Current_Day  # Return the best profit we could make from this day onwards.

            # Start the recursive journey from day 0 with no buy day set yet.  
            return find_Max_Profit_From_Ith_Day(0, -1)
    ```
- ### Approach 2:- Memoization
    ### 🧠 Intuition
    The problem asks us to maximize profit by buying and selling a stock on multiple days. The main idea is to explore the potential profit from each day, considering whether we should buy on that day and sell on a later day. If we can make a profit, we take it; if not, we move on. However, doing this recursively without repeating work is key to finding the optimal solution. 

    ### 🔄 Approach
    The solution utilizes **recursion with memoization** to avoid recalculating the same results over and over again. Here’s how it works:

    1. **Base Case**: If we’ve gone beyond the last day, there’s no more profit to be made. 🎯
    2. **Memoization**: To avoid unnecessary recalculations, we store the results of the maximum profit for each day in a list (`max_Profit_From_Ith_Day`). If we’ve already computed the result for a given day, we simply return it instead of recalculating. 🧠
    3. **Recursive Exploration**: For each day, we calculate the maximum profit by either:
        - **Selling the stock** on that day after buying on a previous day.
        - **Holding onto the stock** and waiting for the next best day to sell (this decision is based on recursion).
    4. **Max Profit Decision**: At each point, we compare the potential profits from selling today versus holding, then pick the best option to maximize profit. 💸

    ### ⏳ Time Complexity
    The time complexity is **$O(n^2)$** due to the recursive calls combined with the loop over the days. We’re trying to sell on all possible days after a given day and recursively checking the best option. Even though memoization reduces redundant calculations, the recursive approach still requires visiting each day and looping through the remaining days.
  
    ### 🧳 Space Complexity
    The space complexity is **$O(n)$** because of the memoization table (`max_Profit_From_Ith_Day`) used to store the maximum profit for each day. Additionally, the recursion stack will have a maximum depth of $n$, where $n$ is the number of days. 

    ### 💻 Code Implementation
    ```python3 []
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
    ```
- ### Approach 3:- Dynamic Programming
    ### 🧠 Intuition
    The problem asks us to maximize profit from buying and selling stock over several days. At each day, we have two possible states:
    - Holding a stock.
    - Not holding a stock (i.e., cash in hand).

    The goal is to find the maximum profit we can achieve by carefully deciding when to buy and sell. We’ll use **dynamic programming (DP)** to track the profit in both states (holding or not holding) and make optimal decisions at each step. 

    ### 🔄 Approach
    We use a **dynamic programming table** (`cash_And_Hold_At_Ith_Day`) to store the maximum profit for each day, depending on whether we’re holding a stock or not. The table has two values for each day:
    1. **cash_And_Hold_At_Ith_Day[day][0]**: Maximum profit when we don't hold a stock (cash in hand).
    2. **cash_And_Hold_At_Ith_Day[day][1]**: Maximum profit when we are holding a stock.

    - ### Steps:
        1. **Initial Setup**: 
            - On Day 0, we either:
                - Start with $0 cash (not holding a stock).
                - Or buy the stock (negative profit initially).
        
        2. **DP Transitions**:
            - For each day after Day 0:
                - **Not holding a stock**: Either continue from the previous day without selling, or sell the stock.
                - **Holding a stock**: Either continue holding the stock, or buy a new stock with the cash from the previous day.
        
        3. **Final Answer**: The answer is the maximum profit on the last day without holding a stock (i.e., cash in hand).

    ### ⏳ Time Complexity
    **$O(n)$**, where $n$ is the number of days. We only need to iterate through the list of prices once, updating the DP table with two values (holding and not holding) at each step. This results in a linear time complexity.

    ### 🧳 Space Complexity
    **$O(n)$**. We use a DP table that stores two values for each day, requiring space proportional to the number of days ($n$). This results in linear space complexity.
  
    ### 💻 Code Implementation
    ```python3 []
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
    ```
- ### Approach 4: Greedy
    ### 🧠 Intuition
    The task is to maximize the profit from buying and selling a stock multiple times, where the goal is to buy low and sell high. You can either hold onto a stock or sell it at any given point. The tricky part is ensuring that you make the best decision at each step. 

    To solve this efficiently, we use **dynamic programming** (DP) to track two possible states for each day:
    1. **Cash**: Maximum profit when not holding any stock (i.e., the money we have in hand).
    2. **Hold**: Maximum profit when we are holding a stock.

    At each step, we make decisions to either:
    - Sell the stock and add the profit to cash.
    - Buy a new stock or continue holding it, updating the hold state.

    The key insight is that at any given time, you’re either holding a stock or not, and these two states evolve independently over time.

    ### 🔄 Approach
    1. **Initial State**: 
        - On Day 0, the initial cash is 0 (no profit, nothing sold).
        - We start with holding the stock, which means an initial negative profit equal to the price of the first stock (`-prices[0]`).
    
    2. **Transitioning States**:
        - For each day, we have two choices:
            1. **Not holding a stock**: We either:
                - Continue with the same amount of cash we had.
                - Sell the stock we’re holding and add the profit (current stock price minus the price at which we bought).
            2. **Holding a stock**: We either:
                - Continue holding the same stock.
                - Buy a new stock by using the cash we have (profit is reduced by the price of the new stock).
    
    3. **Final Answer**: The maximum profit we can achieve is stored in `cash` at the end, as it represents the maximum profit when we do not hold any stock.

    ### ⏳ Time Complexity
    **$O(n)$**, where $n$ is the number of days. We only iterate over the price list once and update the `cash` and `hold` states for each day. This gives us a linear time complexity.

    ### 🧳 Space Complexity
    **$O(1)$**. We only need two variables (`cash` and `hold`) to store the maximum profit in each of the two states. The space used does not depend on the size of the input, so the space complexity is constant.

    ### 💻 Code Implementation
    ```python3 []
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
    ```