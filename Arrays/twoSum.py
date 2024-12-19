def twoSum(target, nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return(i,j)
    return []

def twoSumOP(target, nums):
    num_to_index = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return(num_to_index[complement],i)
        num_to_index[num] = i
    return [] 