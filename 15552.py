import sys

n = int(sys.stdin.readline().rstrip())
calList = [sum(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for e in calList:
    print(e)
