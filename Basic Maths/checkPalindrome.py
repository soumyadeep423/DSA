#Optimal:
def checkPalindrome(n):
    dup = n
    revNum = 0
    ld = 0
    while n > 0:
        ld = n % 10
        revNum = (revNum * 10) + ld
        n = n // 10
    if revNum == dup:
        return True
    else:
        return False

print(checkPalindrome(121))
