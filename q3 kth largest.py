def sort_arr(nums):
    temp = 0
    n = len(nums)
    if n == 2:
        if nums[0] > nums[1]:
            temp = nums[0]
            nums[0] = nums[1]
            nums[1] = temp
            print(nums)
    else:
        n = len(nums) // 2
        nums1 = nums[:n]
        nums2 = nums[n:]
        sort_arr(nums1)
        sort_arr(nums2)

nums = [3, 2, 1, 5, 6, 4, 42, 0]
sort_arr(nums)
print(nums)
