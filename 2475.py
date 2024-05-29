a, b, c, d, e = map(int, input().split())

def cal(a, b, c, d, e):
    f = pow(a, 2) + pow(b, 2) + + pow(c, 2)+ pow(d, 2)+ pow(e, 2)
    return f % 10

print(cal(a, b, c, d, e))