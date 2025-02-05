import sys
import math

t = int(sys.stdin.readline().strip())
rs = []

for _ in range(t):
    m = int(sys.stdin.readline().strip())
    
    if m == 1:
        rs.append("1")
    else:
        count = sum(math.log10(i) for i in range(2, m + 1))
        rs.append(str(int(count) + 1))

sys.stdout.write("\n".join(rs) + "\n")