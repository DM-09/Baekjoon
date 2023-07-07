a, b = map(int, input().split())
def rev(n): return int(str(n)[::-1])
print(rev(rev(a) + rev(b)))
