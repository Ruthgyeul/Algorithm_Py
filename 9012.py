n = int(input())
rs = []

for i in range(n):
    count = 0
    par = list(input())

    for j in range(len(par)):
        if par[j] == "(":
            count += 1
        elif par[j] == ")":
            count -= 1

        if count < 0:
            break  

    if count == 0: 
        rs.append("YES")
    else:
        rs.append("NO")

print("\n".join(rs))