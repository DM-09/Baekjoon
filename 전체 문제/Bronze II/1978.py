def isPrime(n):
    import math

    if n == 1: return False
    if n == 2: return True
    if math.factorial(n - 1) % n == n - 1: return True
    return False

num, N = 0, input()

for i in list(map(int, input().split())):
    if isPrime(i): num += 1

print(num)
