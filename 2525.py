h, m = map(int, input().split())
t = int(input())

dh, dm = divmod(m + t, 60)
h = (h + dh) % 24

print(h, dm)