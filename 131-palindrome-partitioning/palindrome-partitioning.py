class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def dfs(start):
            
            def checkPalindrome(subS):
                return subS == subS[::-1]

            if start == len(s):
                res.append(temp.copy())
            
            for end in range(start + 1, len(s) + 1):
                ss = s[start:end]
                if checkPalindrome(ss):
                    temp.append(ss)
                    dfs(end)
                    temp.pop()
        dfs(0)
        return res