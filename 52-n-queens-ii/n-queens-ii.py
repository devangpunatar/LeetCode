class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diags = set() # (r + c) will be constant 
        neg_diags = set() # (r - c) will be constant
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1 
                return 

            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)

        backtrack(0)
        return res

