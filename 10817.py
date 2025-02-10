def sortM(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sortM(arr[:mid])  
    right = sortM(arr[mid:])  

    return sorted(left + right)

num = list(map(int, input().split()))
numS = sortM(num)

print(numS[1])