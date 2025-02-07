n = [int(input()) for _ in range(10)]
rs = []

for ele in n:
    rs.append(ele % 42)

print(len(set(rs)))