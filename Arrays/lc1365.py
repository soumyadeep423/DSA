def smallerNumbersThanCurrent(nums):
    res = [0] * len(nums)  # Initialize result array with zeros
    for i in range(len(nums)):  # Outer loop for each element
        count = 0
        for j in range(len(nums)):  # Inner loop to compare with every element
            if nums[j] < nums[i]:  # Count elements smaller than nums[i]
                count += 1
        res[i] = count  # Store the count
    return res

def smallerNumbersThanCurrentOP(nums):
    temp = sorted(nums)
    d = {}
    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i
    
    res = []
    for i in nums:
        res.append(d[i])
    return res