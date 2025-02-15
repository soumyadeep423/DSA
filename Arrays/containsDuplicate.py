def containsDuplicate(nums):
    set_nums = set(nums)
    return len(set_nums) != len(nums)