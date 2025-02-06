n, m = map(int, input().split())

nL = {input() for _ in range(n)}
mL = {input() for _ in range(m)}

rs = sorted(nL & mL)

print(len(rs))
print("\n".join(rs))