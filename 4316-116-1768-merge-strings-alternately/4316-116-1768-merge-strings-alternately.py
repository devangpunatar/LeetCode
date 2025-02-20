class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        from itertools import zip_longest
        res = ""

        for c1, c2 in zip_longest(word1, word2, fillvalue = ""):
            res += c1
            res += c2
                
        return res
