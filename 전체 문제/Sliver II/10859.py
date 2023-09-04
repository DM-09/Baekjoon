def isPrime(n):
    import math

    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1

def N(): print('no')

n = input()

if not isPrime(int(n)) or '3' in n or '4' in n or '7' in n: N()
else:
    n = n.replace('6', '!').replace('9', '6').replace('!', '9')
    if isPrime(int(n[::-1])): print('yes')
    else: N()
