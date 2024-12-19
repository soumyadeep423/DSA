def checkSortedBF(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                return False
    return True

def checkSortedBetter(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

def checkSortedandRotated(arr, n):
    count = 0
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count+=1
        if count > 1:
            return False
    return True
