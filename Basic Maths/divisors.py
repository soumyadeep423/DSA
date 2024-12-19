import math
#Brute Force
def printDivisors(n):
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    return divisors

print(printDivisors(128))

#Optimal Approach:
def printDivisorsOP(n):
    divisors = []
    x = int(math.sqrt(n))
    for i in range(1,x+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors

print(printDivisors(128))
