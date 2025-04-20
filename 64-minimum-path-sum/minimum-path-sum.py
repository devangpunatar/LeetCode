class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                elif i == rows - 1 and j != cols - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1]
                elif i != rows - 1 and j == cols - 1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])
                    
        return grid[0][0]







        '''
        2-DP Solution (Tabulation)

        rows, cols = len(grid), len(grid[0])
        dp = [[float('inf') for j in range(cols + 1)] for i in range(rows + 1)]
        dp[rows - 1][cols] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

        '''