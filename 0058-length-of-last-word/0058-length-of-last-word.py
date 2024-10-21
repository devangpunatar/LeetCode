class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        for c in reversed(s):
            if c == ' ' and count > 0:
                break
            elif c != ' ':
                count += 1
        return count