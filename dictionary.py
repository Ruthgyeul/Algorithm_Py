def check(n):
    if n.isdigit() and int(n) > 0:
        n = int(n)
        return n
    else:
        print("You should input a natural number for N.")
        n = input("Please input N: ")
        return check(n)

def cal(nList, start, end):
    if start == end:
        print("".join(map(str, nList)))
    else:
        for i in range(start, end + 1):
            nList[start], nList[i] = nList[i], nList[start]
            cal(nList, start + 1, end)
            nList[start], nList[i] = nList[i], nList[start]

n = check(input("Please input N: "))

nList = list(range(1, n + 1))
cal(nList, 0, n - 1)
