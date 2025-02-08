import sys
from collections import deque

n = int(sys.stdin.readline().strip())
rs = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        rs.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(rs.popleft() if rs else -1)
    elif cmd[0] == "size":
        print(len(rs))
    elif cmd[0] == "empty":
        print(1 if not rs else 0)
    elif cmd[0] == "front":
        print(rs[0] if rs else -1)
    elif cmd[0] == "back":
        print(rs[-1] if rs else -1)