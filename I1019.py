import sys

def count(n):
    counts = [0] * 10
    
    for i in range(1, n+1):
        for digit in str(i):
            counts[int(digit)] += 1

    return counts

n = int(sys.stdin.readline().rstrip())

result = count(n)
print(' '.join(map(str, result)))
