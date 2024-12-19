import math
#Brute Force:
def countDigits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def countDigitsOP(n):
    count = int(math.log10(n))
    return count+1

print(countDigitsOP(423))

#Optimal:
def countDigitsOP(n):
    count = int(math.log10(n))
    return count+1

print(countDigitsOP(423))
