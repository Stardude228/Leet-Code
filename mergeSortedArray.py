# mergeSortedArray completed by Oomat Latipov
def mergeSortedArray():
    nums1 = [1,2,3,0,0,0]
    m = 3 
    nums2 = [2,5,6]
    n = 3
    
    nums1 = nums1[:m]
    nums1.extend(nums2[:n])
    
    nums1.sort()
    print(nums1)

mergeSortedArray()

# Leet Code version of mergeSortedArray
def mergeSortedArray():
    
    nums1 = [1,2,3,0,0,0]
    m = 3 
    nums2 = [2,5,6]
    n = 3
    
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while (j >= 0):
        if (i >= 0 and nums1[i] > nums2[j]):
            nums1[k] = nums1[i]
            k -=1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
mergeSortedArray()