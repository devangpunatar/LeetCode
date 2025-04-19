class Solution:
    def fib(self, n: int) -> int:
        # Recursive Solution

        # if n == 0 or n == 1:
        #     return n

        # return self.fib(n - 1) + self.fib(n - 2)

        # Top Down DP (Memoization)

        memo = {0: 0, 1: 1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
                return memo[x]

        return f(n)
