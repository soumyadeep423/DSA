def armstrong(n):
    dup = n
    sum = 0
    ld = 0
    k = len(str(n))
    while n > 0:
        ld = n % 10
        sum += ld ** k
        n = n // 10
    return sum == dup
