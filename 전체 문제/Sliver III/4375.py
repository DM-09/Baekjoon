while True:
    try: i = int(input())
    except: break
    
    s = ''

    while True:
        s += '1'
        if int(s) % i == 0:
            print(len(s))
            break
