def missingNumber(nums):
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return num - 1
        if num == len(nums) - 1:
            return num + 1

def missingNumberOP(nums):
    return sum(range(len(nums)+1)) - sum(nums)

