class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0

        def dfs(r, c):
            if (r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == "0" or (r, c) in visited):
                return 

            visited.add((r, c))
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands                