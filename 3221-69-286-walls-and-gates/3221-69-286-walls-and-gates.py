class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or
                (r, c) in visited or rooms[r][c] == -1):
                return
            visited.add((r, c))
            q.append([r, c]) 

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist # we know already that gates are 0, but in the next for loop there will be values in queue whose distance will be 1
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
