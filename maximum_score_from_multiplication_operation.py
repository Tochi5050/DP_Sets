class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        # memo = {}
        @lru_cache(2000)
        def dp(op, left):
            if op == m:
                return 0

            # If already computed, return
            # if (op, left) in memo:
            #     return memo[(op, left)]

            # print(l, 'l', nums[left], 'nums[left]', multipliers[op], 'multipliers[op]', op, 'op')
            l = nums[left] * multipliers[op] + dp(op + 1, left + 1)
            # print(l, 'l', op, 'op', nums[left] , 'nums[left] ', multipliers[op], "multipliers[op]")
            r = nums[(n - 1) - (op - left)] * multipliers[op] + dp(op + 1, left)
            # print(r, 'r', op, 'op', nums[(n-1)-(op-left)] , 'nums[(n-1)-(op-left)] ', multipliers[op], "multipliers[op]")
            # print(max(l, r), 'max(l, r)', op, 'op', l , 'l ', r, "r")

            return max(l, r)

            # memo[(op, left)] = max(l, r)

            # return memo[(op, left)]

        # Zero operation done in the beginning
        return dp(0, 0)
