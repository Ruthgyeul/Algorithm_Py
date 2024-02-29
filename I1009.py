test = int(input())
results = []

for _ in range(test):
    num1, num2 = map(int, input().split())
    results.append((num1 ** num2) % 10)

for result in results:
    print(result)
