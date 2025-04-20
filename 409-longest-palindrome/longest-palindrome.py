class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = {}
        res = 0
        for char in s:
            count[char] = 1 + count.get(char, 0)
        
        for char in count:
            if count[char] > 1:
                if count[char] % 2 == 0:
                    temp = count[char]
                else:
                    temp = count[char] - 1
                count[char] -= temp
                res += temp
        return res + 1 if sum(count.values()) > 0 else res


                

        