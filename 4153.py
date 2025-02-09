rs = []

while True:
    tri = list(map(int, input().split()))

    if tri[0] == tri[1] == tri[2] == 0:
        print("\n".join(rs))
        break
    else:
        tri.sort()
        if tri[2]**2 == (tri[0] ** 2 + tri[1] ** 2):
            rs.append("right")
        else:
            rs.append("wrong")