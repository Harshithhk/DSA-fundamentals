def mergesort(arr, left, right):
    sorted_arr = []
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)
        sorted_arr = merge(arr, left, mid, right)
    return sorted_arr


def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            B[k] = arr[i]
            i = i + 1
        else:
            B[k] = arr[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        B[k] = arr[i]
        i = i + 1
        k = k + 1

    while j <= right:
        B[k] = arr[j]
        j = j + 1
        k = +1

    for x in range(left, right + 1):
        arr[x] = B[x]

    return arr


input_arr = [3, 5, 8, 9, 6, 2]

sorted_arr = mergesort(input_arr, 0, len(input_arr) - 1)

print(sorted_arr)
