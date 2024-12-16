n, x = map(int, input().split())
a = list(map(int, input().split()))
rs =[]

for e in a:
    if (int(e) < x):
        rs.append(str(e))
print(' '.join(rs))