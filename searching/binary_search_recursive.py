import math


def bin_search_rec(nums, n, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if n == nums[mid]:
        return mid
    elif n < nums[mid]:
        return bin_search_rec(nums, n, left, mid - 1)
    elif n > nums[mid]:
        return bin_search_rec(nums, n, mid + 1, right)


nums = [1, 2, 3, 4, 5, 6]

num = input("Enter Number: ")
n = int(num)
print(bin_search_rec(nums, n, 0, (len(nums) - 1)))
