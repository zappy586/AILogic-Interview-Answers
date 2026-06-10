def find_peak_element(nums):
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
            return i

# test 1
nums = [1, 2, 3, 1]
print(find_peak_element(nums)) 

#test 2
nums = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(nums))