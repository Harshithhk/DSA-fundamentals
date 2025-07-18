def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = value
    return arr


nums = [1, 4, 2, 5, 3, 7, 4]

sorted_arr = insertionsort(nums)
print(sorted_arr)
