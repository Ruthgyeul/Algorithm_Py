import sys

def mergeCount(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return count

def mergeSortCount(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2

        count += mergeSortCount(arr, temp, left, mid)
        count += mergeSortCount(arr, temp, mid + 1, right)
        count += mergeCount(arr, temp, left, mid, right)

    return count

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

temp = [0] * n

print(mergeSortCount(arr, temp, 0, n - 1))