class Solution:
    def validPalindrome(self, s: str, strike=False) -> bool:
    
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if strike:
                    return False
                return self.validPalindrome(s[l:r], True) or self.validPalindrome(s[l + 1:r + 1], True)
            else:
                l += 1
                r -= 1
        return True