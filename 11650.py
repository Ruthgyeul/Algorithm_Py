def sort(arr, left, right):
    if left >= right:
        return
    
    pivot = arr[(left + right) // 2]
    i, j = left, right
    
    while i <= j:
        while arr[i][0] < pivot[0] or (arr[i][0] == pivot[0] and arr[i][1] < pivot[1]):
            i += 1
        while arr[j][0] > pivot[0] or (arr[j][0] == pivot[0] and arr[j][1] > pivot[1]):
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    sort(arr, left, j)
    sort(arr, i, right)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

sort(xy, 0, n - 1)

for row in xy:
    print(row[0], row[1])