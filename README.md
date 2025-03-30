# 📈 [The Stock Market Adventure!](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii?envType=study-plan-v2&envId=top-interview-150) 🚀

**Type:** Medium 💪 <br>
**Topics:** Array 📋🔢, Dynamic Programming 🗂️🔄, Greedy 🥇💸
<hr>

Imagine you’re in a **stock market rollercoaster** 🎢, and your goal is to make the **maximum profit** while keeping your sanity intact.

You’re given an array of **$prices$**, where each number represents the **price of a stock on a particular day**. 📊 Think of it like a series of “buy-low, sell-high” opportunities… except you’re not a psychic 🧙‍♂️—just a clever investor with quick reflexes!

**Here’s the catch:**
- You can **buy** a stock, then **sell it immediately** on the same day. (Because who likes holding onto stuff, right? 🤷‍♂️)
- You can only **hold ONE share** at a time. No stock hoarding here! 🛒🚫

Your job? **Find the maximum profit you can make** without becoming a stock market wizard. 🔮💼

### Examples 📊
- **Example 1:** <br>
**Input:** **$[7,1,5,3,6,4]$** <br>
**Story:** You buy at **$1$** (because it’s a steal 😎), sell at **$5$** (cha-ching! 💰), then buy at **$3$** (low key, but hey), and sell at **$6$** (profit dance time 💃). <br>
**Profit**: **$7$** 💥 (you’re basically a stock market ninja now.)

- **Example 2:** <br>
**Input:** **$[1,2,3,4,5]$** <br>
**Story:** Buy at **$1$** (because why not?), and sell at **$5$** (the ultimate glow-up ✨). <br>
**Profit:** **$4$** 🤑 (because you know how to ride the wave without crashing.)

- **Example 3:** <br>
**Input:** **$[7,6,4,3,1]$** <br>
**Story:** No matter how hard you try, the prices just keep falling. 😞 <br>
**Profit:** **$0$** (sometimes, the best move is to just not buy—like avoiding a bad date. 🚫❤️)

### Constraints (AKA The Rules of the Game) 🎯
- $1 \leq prices.length \leq 3 \times 10^4$ 🚀
(You can have anywhere from 1 to 30,000 days of stock prices. That’s a lot of coffee-fueled decision-making! ☕📈)
- $0 \leq prices[i] \leq 10^4$ 💰
(Stock prices range from $\$0$ to $\$10,000$. So, whether it’s a budget buy or a luxury splurge, you’ve got options! 😎)