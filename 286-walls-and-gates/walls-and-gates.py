class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        dist = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or r == rows or c < 0 or c == cols or rooms[r][c] == -1):
                        continue
                    if rooms[r][c] == 2147483647:
                        rooms[r][c] = dist
                        q.append((r, c))
            dist += 1