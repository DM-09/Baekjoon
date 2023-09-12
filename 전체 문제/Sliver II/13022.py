s = input()

def wolf(s):
    if len(s) == 0: return 1
    try:
        i = [s.index('o'), s.index('l'), s.index('f')]
        fn = 0
        w = len(s[:i[0]])

        for j in s[i[2]:]:
            if j != 'f': break
            fn += 1

        o = len(s[i[0]:i[1]])
        l = len(s[i[1]:i[2]])
        f = len(s[i[2]:i[2] + fn])

        if w == o == l == f: return i[2] + fn
    except: pass

    return 0

r = wolf(s)

while 1:
    if len(s) == 0 or r == 0: break
    else: s = s[r:]
    r = wolf(s)

print(0 if r == 0 else 1)
