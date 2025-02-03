a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)
counts = [0] * 10

for digit in result:
    counts[int(digit)] += 1

for count in counts:
    print(count)