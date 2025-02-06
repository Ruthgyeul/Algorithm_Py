def wood(h, saw):
    return sum(tree - saw for tree in h if tree > saw)

def saw(h, m):
    minS, maxS = 0, max(h)
    best = 0

    while minS <= maxS:
        midS = (minS + maxS) // 2
        woodC = wood(h, midS)

        if woodC >= m:
            best = midS
            minS = midS + 1
        else:
            maxS = midS - 1

    return best

n, m = map(int, input().split())
h = list(map(int, input().split()))

print(saw(h, m))