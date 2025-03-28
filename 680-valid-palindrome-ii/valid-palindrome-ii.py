class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s, l, r):
            return s[l:r+1] == s[l:r+1][::-1]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return check(s, l + 1, r) or check(s, l, r - 1)
            l += 1
            r -= 1
        return True
