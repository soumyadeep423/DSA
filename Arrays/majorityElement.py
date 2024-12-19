from collections import defaultdict

def majority(arr):
    arr.sort()
    return arr[int(len(arr)/2)]

def majorityBetter(arr):
    m = defaultdict(int)
    for num in arr:
        m[num]+=1
    for key,value in m.items():
        if value > len(arr)/2:
            return key
    return 0

# Moore's Voting Algorithm
def majorityOP(arr):
    count = 0
    candidate = 0
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count+=1
        else:
            count-=1
    return candidate

