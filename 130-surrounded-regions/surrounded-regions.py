class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O'):
                return
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)    

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'