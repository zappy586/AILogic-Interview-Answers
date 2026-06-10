def sort_arr(nums, k):
    n = len(nums)
    temp = 0
    i, j = 0, 1
    while j < n:
        print(nums)
        if nums[i] > nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j += 1
        else:
            i += 1
    return nums[k]

nums = [3, 2, 1, 5, 6, 4]
print(sort_arr(nums, 2))
