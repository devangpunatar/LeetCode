class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
       
        for row in range(rows):
            for col in range(cols):

                live_neighbours = 0
                for neighbour in neighbours:
                    r = (row + neighbour[0])
                    c = (col + neighbour[1])
                    # we count the number of live neighbours for each board[row][col]
                    if (r >= 0 and r < rows) and (c >= 0 and c < cols) and (copy_board[r][c] == 1):
                        live_neighbours += 1
                
                if copy_board[row][col] == 1 and (live_neighbours > 3 or live_neighbours < 2):
                    board[row][col] = 0

                if copy_board[row][col] == 0 and live_neighbours == 3:
                    board[row][col] = 1
