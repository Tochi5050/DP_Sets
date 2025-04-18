from typing import List

class Solution:  #print(Solution.maxProfit(2, [6, 5, 3, 2, 0, 3]))
    def maxProfit(k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for __ in range(n + 1)]
        # print(dp)

        for i in range(n - 1, -1, -1):
            for transactions_remaining in range(1, k + 1):
                for holding in range(2):
                    do_nothing = dp[i + 1][transactions_remaining][holding]
                    if holding:
                        # Sell stock
                        do_something = prices[i] + dp[i + 1][transactions_remaining - 1][0]
                    else:
                        # Buy stock
                        do_something = -prices[i] + dp[i + 1][transactions_remaining][1]

                    # Recurrence relation
                    dp[i][transactions_remaining][holding] = max(do_nothing, do_something)
        print(dp, i, holding)
        return dp[0][k][0]

print(Solution.maxProfit(4, [3,2,6,5,0,3]))