n = int(input())

for _ in range(n):
    score = input()
    total = cont = 0

    for ele in score:
        if ele == "O":
            cont += 1
            total += cont
        else:
            cont = 0
    print(total)