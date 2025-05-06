class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rookRow, rookCol = r, c
                    break
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 
        res = 0

        for dr, dc in directions:
            r, c = rookRow + dr, rookCol + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':
                    break
                if board[r][c] == 'p':
                    res += 1
                    break
                r += dr
                c += dc
        return res