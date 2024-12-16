t = int(input())
rs = []

for i in range(t):
    a, b = map(int, input().split())
    rs.append(a + b)

for x in rs:
    print(x)