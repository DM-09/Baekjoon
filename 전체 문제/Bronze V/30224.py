n = int(input())

def solve(n):
    if str(n).count('7') == 0 and n % 7 != 0: return 0
    if str(n).count('7') == 0 and n % 7 == 0: return 1
    if str(n).count('7') != 0 and n % 7 != 0: return 2
    if str(n).count('7') != 0 and n % 7 == 0: return 3

print(solve(n))
