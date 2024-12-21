def rotateArr1(arr,k):
    n = len(arr)
    k = k % n
    rotated = [0] * n
    for i in range(n):
        rotated[(i+k) % n] = arr[i]
    for i in range(n):
        arr[i] = rotated[i]
    return arr

def rotateArr2(arr,k):
    n = len(arr)
    k = k % n
    arr[:k], arr[k:] = arr[-k:], arr[:-k]
    return arr

def rotateArr3(arr,k):
    n = len(arr)
    k = k % n
    def reverse(left,right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    return arr

