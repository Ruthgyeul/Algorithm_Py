n = int(input())

for i in range(n):
    print(" " * (n - (i + 1)) + "*"+"**"*i)

for i in range(n-1):
    print(" " * (i+1) + "*"+"**"*(n-2-i))