
def search_insert(nums, target):
    if target in nums:
        return nums.index(target)
    if target == 0 or target <= nums[0]:
        return 0    
    
    for i, num in enumerate(nums):
        if target > nums[-1]:
            return len(nums)
        elif target >= num and target < nums[i+1]:
            return i + 1

print(search_insert([1,3,5,6], 2))