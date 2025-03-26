class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        return count['R'] == count['L'] and count['U'] == count['D']
