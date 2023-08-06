l = [int(input()) for _ in range(5)]

def solve():
    re = l[0]
    try:
        l.remove(re)
        l.remove(re)
    except: print(re); return

    re = l[0]
    try:
        l.remove(re)
        l.remove(re)
    except: print(re); return
    print(*l)
    
solve()
