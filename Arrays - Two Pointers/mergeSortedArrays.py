def mergeArr(arr1,m,arr2,n):
    for i in range(n):
        arr1[m+i] = arr2[i]
    arr1.sort()
    return arr1

def mergeArrOP(arr1,m,arr2,n):
    i = m-1
    j = n-1
    k = m+n-1
    while j>= 0:
        if i>=0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i-=1
        else:
            arr1[k] = arr2[j]
            j-=1
        k-=1
    return arr1
