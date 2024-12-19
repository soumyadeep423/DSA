#Brute Force:
def gcd(m,n):
    gcd = 1
    for i in range(1, min(m,n)+1):
        if n%i == 0 and m%i==0:
            gcd = i
    return gcd

print(gcd(42,77))

#Better Approach:
def gcdBetter(m,n):
    gcd = 1
    for i in range(min(m,n), 0, -1):
        if n%i==0 and m%i==0:
            return i  
    return 1

print(gcdBetter(42,77))

#Optimal: Euclidean Algorithm
def gcdOP(m,n):
    while n>0 and m>0:
        if n < m:
            m = m % n
        else:
            n = n % m
    if m==0:
        return n
    return m

print(gcdOP(42,77))