from collections import deque
def sortedSquares(nums):
    res = deque()
    left_pointer, right_pointer = 0, len(nums) - 1
    while left_pointer <= right_pointer:
        left_value, right_value = abs(nums[left_pointer]), abs(nums[right_pointer])
        if left_value > right_value:
            res.appendleft(left_value * left_value)
            left_pointer += 1
        else:
            res.appendleft(right_value * right_value)
            right_pointer -= 1
    return list(res)