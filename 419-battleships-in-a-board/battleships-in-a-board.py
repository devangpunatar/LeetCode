class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                # Count only the first cell of a ship (top-left most)
                if board[r][c] == 'X':
                    if (r > 0 and board[r - 1][c] == 'X') or (c > 0 and board[r][c - 1] == 'X'):
                        continue  # Skip if it's a continuation of a ship
                    res += 1

        return res
