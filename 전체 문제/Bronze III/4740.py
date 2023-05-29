while True:
    i = input()
    if i == "***":
        break
    print(''.join(reversed(list(i))))
