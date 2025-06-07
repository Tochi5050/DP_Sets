from typing import List
from functools import lru_cache


class Solution:
    def minPathSum(grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)

        @lru_cache
        def dp(row, col):
            if row == m or col == n:
                return float('inf')

            if row == m - 1 and col == n - 1:
                return grid[row][col]
            print("row", row, "col", col, "grid[row][col] =>", grid[row][col], "dp(row + 1, col) =>", dp(row + 1, col), "dp(grid, i, j + 1) =>", dp(row, col + 1))
            return grid[row][col] + min(dp(row + 1, col), dp(row, col + 1))

        return dp(0, 0)


# print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(Solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))