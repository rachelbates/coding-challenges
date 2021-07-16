nums = [0,1,2,2,3,0,4,2]
val = 2

def remove_element(nums, val):
    while val in nums:
        placements = nums.index(val)
        nums.pop(placements)
    
    print(nums)

remove_element(nums, val)