def bin_search(nums, n):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == n:
            return mid
        if nums[mid] < n:
            left = mid + 1
        if nums[mid] > n:
            right = mid - 1

    return -1


nums = [1, 2, 3, 4, 5, 6]

num = input("Enter Number: ")
n = int(num)
print(bin_search(nums, n))
