n = [list(map(int, input().split())) for _ in range(9)]
high = 0
r, c = 0, 0

for i in range(9):
    for j in range(9):
        num = n[i][j]
        if high <= num:
            high = num
            r = i + 1
            c = j + 1

print(high)
print(r, c)