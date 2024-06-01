import sys

n = int(sys.stdin.readline().strip())
result = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())

    data = pow(a, b)
    result.append(data%10)
    
for ele in result:
    print(ele)