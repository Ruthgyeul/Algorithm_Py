import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())
rs = []

for num in range(m, n+1):
    if prime(num):
        rs.append(num)

print("\n".join(map(str, rs)))