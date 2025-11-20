# removeElement completed by Oomat Latipov
def removeElement():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    
    for i in nums[:]:
        if i == val:
            nums.remove(i)
    
    k = len(nums)
    print(k, nums)

removeElement()

# Leet Code version of removeElement
def removeElement():

    nums = [0,1,2,2,3,0,4,2]
    val = 2

    l, r = 0, len(nums)

    while l < r:
        if nums[l] == val:
            nums[l] = nums[r - 1]
            r -= 1
        else:
            l += 1
    return r
removeElement()
