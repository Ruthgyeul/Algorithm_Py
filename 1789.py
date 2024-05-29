num = int(input())
n = 0
count = 0

while num > 0:
    n = n + 1
    num = num - (n + 1)
    count = count + 1

print(count - 1)