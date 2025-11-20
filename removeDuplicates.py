# removeDuplicates completed by Oomat Latipov
def removeDuplicates():
    nums = [1,1,2]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    
    k, l, r = 0, 0, 1
    
    while r < len(nums):
        if nums[r] == nums[l]:
            nums.pop(r)
        else:
            l += 1
            r += 1
        k = len(nums)
    
    print(k, nums)

removeDuplicates()


# Leet Code version of removeDuplicates
def removeDuplicates():
    nums = [1,1,2]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    
    true_i = 1
    new_i = 1
    while true_i < len(nums):
        if nums[true_i] != nums[new_i - 1]:
            nums[true_i], nums[new_i] = nums[new_i], nums[true_i]
            new_i += 1
        true_i += 1
    return new_i

removeDuplicates()