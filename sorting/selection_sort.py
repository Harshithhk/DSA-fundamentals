def selectionsort(arr):
    n = len(arr)
    for i in range(n - 1):
        position = i
        for j in range(i + 1, n):
            if arr[j] < arr[position]:
                position = j
        temp = arr[i]
        arr[i] = arr[position]
        arr[position] = temp

    return arr


nums = [1, 4, 2, 5, 3, 7, 4]

sorted_arr = selectionsort(nums)
print(sorted_arr)
