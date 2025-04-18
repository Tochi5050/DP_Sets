from typing import List
from functools import lru_cache


class Solution: # print(Solution.maxProfit(2, [6, 5, 3, 2, 0, 3]))
    def maxProfit(k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, transactions_remaining, holding):
            # Base case
            # print(lru_cache(None))
            if transactions_remaining == 0 or i == len(prices):
                return 0

            print("transactions_remaining->>", transactions_remaining , "i->>>", i, "holding=", holding )
            do_nothing = dp(i + 1, transactions_remaining, holding)
            print("do_nothing=", do_nothing, "i=", i)
            do_something = 0

            if holding:
                # Sell stock
                print("i=", i, "prices[i]=", prices[i], "i + 1=", i + 1, "transactions_remaining=", transactions_remaining - 1, "Holding=", holding)
                do_something = prices[i] + dp(i + 1, transactions_remaining - 1, 0)
            else:
                # Buy stock
                print("i=", i, "-prices[i]=", -prices[i], "i + 1=", i + 1, "transactions_remaining=", transactions_remaining, "Holding=", holding )
                do_something = -prices[i] + dp(i + 1, transactions_remaining, 1)

            # Recurrence relation
            print("do_nothing=", do_nothing, "do_something", do_something, "max_do_nothing->>", max(do_nothing, do_something), "i->>>", i)
            return max(do_nothing, do_something)

        return dp(0, k, 0)

# print(Solution.maxProfit(2, [2,4,1]))
# print(Solution.maxProfit(2, [6, 5, 3, 2, 0, 3]))
print(Solution.maxProfit(4, [3,2,6,5,0,3]))


