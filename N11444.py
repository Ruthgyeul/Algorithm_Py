import sys

MOD = 1000000007
memo = {0: 0, 1: 1}

def fib(n):
    if n in memo:
        return memo[n]
    
    if n % 2 == 0:
        k = n // 2
        memo[n] = (fib(k) * (2 * fib(k - 1) + fib(k))) % MOD
    else:
        k = (n + 1) // 2
        memo[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1)) % MOD
    
    return memo[n]

n = int(sys.stdin.readline().strip())
print(fib(n))