def removeElement(arr, val):
    j = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[j] = arr[i]
            j+=1
    return(arr[:j])