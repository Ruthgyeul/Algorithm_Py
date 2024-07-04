import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = [int(data[i]) for i in range(1, n + 1)]

arr.sort()

sys.stdout.write("\n".join(map(str, arr)) + "\n")