s = input()
abc = "abcdefghijklmnopqrstuvwxyz"
rs = [0] * 26

for i in range(len(abc)):
    rs[i] = s.find(abc[i])

print(" ".join(map(str, rs)))