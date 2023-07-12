class Solution:
    def fib(self, n: int) -> int:
        def fib(n):
            dp=[-1]*(n+1)
            if n==0:
                return 0
            if n==1:
                return 1
            elif dp[n]!=-1:
                return dp[n]
            else:
                dp[n]=fib(n-1)+fib(n-2)
                return dp[n]
        return fib(n)