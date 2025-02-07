import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
num = map(int, input().split())

rs = sum(1 for ele in num if prime(ele))

print(rs)