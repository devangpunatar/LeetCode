class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in `s`
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Decrement counts based on characters in `t`
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        # If all counts are zero, they are anagrams
        return True
