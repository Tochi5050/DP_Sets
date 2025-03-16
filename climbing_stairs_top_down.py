class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def climbStairsHelper(n, memo):
            # if n  == 2:
            #     return 1
            if n in memo:
                return memo[n]

            if n == 1:
                return 1

            if n == 0:
                return 1

            memo[n] = climbStairsHelper(n - 1, memo) + climbStairsHelper(n - 2, memo)
            return memo[n]

        return climbStairsHelper(n, memo)