def fibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)
    
    dp0[0], dp1[0] = 1, 0
    dp0[1], dp1[1] = 0, 1
    
    for i in range(2, n + 1):
        dp0[i] = dp0[i - 1] + dp0[i - 2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]
    
    return dp0[n], dp1[n]

n = int(input())
num = [int(input()) for _ in range(n)]

for i in num:
    print(*fibo(i))