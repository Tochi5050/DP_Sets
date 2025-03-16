def max_score(nums, multiplier):
    m = len(multiplier)
    n = len(nums)
    dp = [[0] * (m + 1) for _ in range((m + 1))]

    for i in range(m - 1, -1, -1):
        for left in range(i, -1, -1):
            mult = multiplier[i]
            right = n - 1 - (i - left)
            dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], mult * nums[right] + dp[i + 1][left])
    print(dp)
    return dp[0][0]



nums = [3,2,1]
multipliers = [1, 2, 3]
max_score(nums, multipliers)

