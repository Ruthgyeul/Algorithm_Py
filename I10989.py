def sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    rs = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rs.append(left[i])
            i += 1
        else:
            rs.append(right[j])
            j += 1
    rs.extend(left[i:])
    rs.extend(right[j:])
    return rs

n = int(input())
nL = [int(input()) for _ in range(n)]

print("\n".join(map(str, sort(nL))))