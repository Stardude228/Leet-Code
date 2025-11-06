# twoSum completed by Oomat Latipov
nums = [3,2,3]
def twoSum(nums):
    target = 6
    for a in range(len(nums) - 1):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]
twoSum(nums)

# optimized version of twoSum (Leet Code)
nums = [3,2,3]
def twoSum(nums):
    target = 6
    mp = {}
    for i,val in enumerate(nums):
        diff = target - val
        if diff in mp:
            return [mp[diff],i]
        mp[val] = i
twoSum(nums)