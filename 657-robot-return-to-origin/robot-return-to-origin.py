class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for m in moves:
            if m == "R":
                x += 1
            if m == "L":
                x -= 1
            if m == "U":
                y += 1
            if m == "D":
                y -= 1
        
        if x == y == 0:
            return True
        else:
            return False