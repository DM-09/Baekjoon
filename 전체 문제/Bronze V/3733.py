while True:
    try:
        s, x = map(int, input().split())
        print(x // (s + 1))
    except:
        break
