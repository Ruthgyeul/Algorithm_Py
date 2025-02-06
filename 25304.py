total = int(input())
prod = int(input())
check = 0

for _ in range(prod):
    pric, n = map(int, input().split())
    check += pric * n

if total == check:
    print("Yes")
else:
    print("No")