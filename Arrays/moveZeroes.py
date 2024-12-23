def moveZeroes(nums):
    n = len(nums)
    non_zero_pos = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1
    for i in range(non_zero_pos,n):
        nums[i] = 0
    return nums

def moveZeroesOP(nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    if j==-1:
        return nums
    for i in range(j+1,len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1
    return nums