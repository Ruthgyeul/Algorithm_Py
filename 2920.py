n = list(map(int, input().split()))
r = sorted(n)

if n == r:
    print("ascending")
elif n == r[::-1]:
    print("descending")
else:
    print("mixed")