# 달팽이 불쌍해...
a, b, v = map(int, input().split())

day = (v - b - 1) // (a - b) + 1
print(day)