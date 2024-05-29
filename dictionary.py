def check(n):
    if n.isdigit() and int(n) > 0:
        return int(n)
    else:
        print("You should input a natural number for N.")
        return check(input("Please input N: "))

def cal(nList, start, end):
    if start == end:
        result = ""
        for num in nList:
            result += str(num)
        print(result)
    else:
        for i in range(start, end + 1):
            nList[start], nList[i] = nList[i], nList[start]
            cal(nList, start + 1, end)

n = check(input("Please input N: "))

nList = list(range(1, n + 1))
cal(nList, 0, n - 1)