def maxArr(arr):
    arr.sort()
    return arr[-1]


def maxArrOP(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max
