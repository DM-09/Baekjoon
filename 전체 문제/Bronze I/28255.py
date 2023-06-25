import math


def tail(S): return S[1:]
def rev(S): return ''.join(reversed(S))
def ceil(N): return math.ceil(N)
def p1(): print(1)


for _ in range(int(input())):
    S = input()
    Sr = S[:ceil(len(S) / 3)]

    if S == Sr + rev(Sr) + Sr: p1()
    elif S == Sr + tail(rev(Sr)) + Sr: p1()
    elif S == Sr + rev(Sr) + tail(Sr): p1()
    elif S == Sr + tail(rev(Sr)) + tail(Sr): p1()
    else: print(0)
