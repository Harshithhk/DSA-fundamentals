def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


nums = [1, 10, 7, 4, 5]
sorted_arr = bubblesort(nums)
print(sorted_arr)
