#Optimal
def reverseNum(n):
    x = abs(n)
    revNum = 0
    ld = 0
    sign = 1 if n > 0 else -1
    while x > 0:
        ld = x % 10
        revNum = (revNum*10) + ld
        x = x // 10
    return revNum*sign

print(reverseNum(-423))