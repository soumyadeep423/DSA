import math
#Brute Force:
def checkPrime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count+=1
    if count == 2:
        return True
    else:
        return False
    
print(checkPrime(7))

#Optimal Approach:
def checkPrimeOP(n):
    count = 0
    x = int(math.sqrt(n))
    for i in range(1,x+1):
        if n%i==0:
            count+=1
            if i != n//i:
                count+=1
    if count == 2:
        return True
    else:
        return False
    
print(checkPrimeOP(7))
