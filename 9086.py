n = int(input())
output = []

for i in range(n):
    strL = input()
    rs = strL[0] + strL[-1]
    output.append(rs)

for e in output:
    print(e)