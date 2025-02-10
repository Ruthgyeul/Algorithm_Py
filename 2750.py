def sortM(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sortM(arr[:mid])  
    right = sortM(arr[mid:])  

    return sorted(left + right)

n = int(input())
num = [int(input()) for _ in range(n)]

print("\n".join(map(str, sortM(num))))