while True:
    try:
        i = input()
        while i.count('BUG') != 0:
            i = i.replace('BUG', '')
        print(i)
    except: break
