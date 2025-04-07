class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, res = 0, 0
        char_count = {'a': 0, 'b': 0, 'c': 0}

        for r in range(len(s)):
            char_count[s[r]] += 1
            
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                res += len(s) - r
                char_count[s[l]] -= 1
                l += 1

        return res