class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) - 1  # 3
        n = len(obstacleGrid[0]) - 1  # 3
        start_row = 0
        start_col = 0
        memo = {}
        return self.uniquePathsWithObstaclesHelper(obstacleGrid, start_row, start_col, m, n, memo)

    def uniquePathsWithObstaclesHelper(self, obstacleGrid, start_row, start_col, m, n, memo):
        grid = start_row, start_col

        if grid in memo:
            return memo[grid]

        if start_row > m or start_col > n:
            return 0

        obstacle = obstacleGrid[start_row][start_col]

        if obstacle == 1:
            return 0

        if start_row == m and start_col == n:
            return 1

        memo[grid] = self.uniquePathsWithObstaclesHelper(obstacleGrid, start_row + 1, start_col, m, n,memo) + self.uniquePathsWithObstaclesHelper(obstacleGrid,start_row,start_col + 1, m,n, memo)

        return memo[grid]



