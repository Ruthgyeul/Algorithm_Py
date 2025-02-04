n = int(input())
a = set(map(int, input().split()))
m = int(input())
lm = map(int, input().split())

result = ["1" if num in a else "0" for num in lm]

print("\n".join(result))