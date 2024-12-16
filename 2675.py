t = int(input())
p1, p2 = [], []

for i in range(t):
    r, s = map(str, input().split())
    for x in s:
        p1.append(x * int(r))
    p2.append(''.join(p1))
    p1 = []
    
print('\n'.join(p2))