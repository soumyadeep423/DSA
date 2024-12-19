def removeDuplicates(arr):
    j = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
    return j

def removeDuplicatesII(nums):
    j = 1
    for i in range(1, len(nums)):
        if j==1 or nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j+=1
    print(j)