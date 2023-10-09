n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def s(a : list, b: list):
    a.sort(reverse=1)
    b.sort()
    t = 0

    for i in range(len(a)):
        t += a[i] * b[i]

    return t

print(s(a, b))
