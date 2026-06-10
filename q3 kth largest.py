def sort_arr(nums, k):
    n = len(nums)
    temp = 0
    i, j = 0, n - 1
    while i < j:
        print(nums)
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
        else:
            j -= 1
    return nums[k]

nums = [3, 2, 1, 5, 6, 4, 42, 0]
print(sort_arr(nums, 2))
