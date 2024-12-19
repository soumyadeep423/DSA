def secondLargest(arr):
    arr.sort()
    return arr[len(arr)-2]

def secondLargestBetter(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for num in arr:
        largest = max(largest, num)
    for num in arr:
        if num > secondLargest and num != largest:
            secondLargest = num
    return secondLargest

def secondLargestOP(arr):
    largest = float('-inf')
    secondLargest = float('-inf')
    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
    return secondLargest
