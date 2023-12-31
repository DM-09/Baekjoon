s = input()
d = {}

for i in range(len(s)):
    try: d[s[i]].append(i); d[s[i]].sort()
    except: d[s[i]] = [i]

l = ['' for _ in range(len(s))]

def f(head : str, tail : str):
    if head == '' and tail == '': return
    if tail == '':
        a = sorted(set(list(head)))[0]
        ind = d[a].pop()

        l[ind] = a
        print(''.join(l))

        ind = head.index(a)
        f(head[:ind], head[ind+1:])
    else:
        a = sorted(set(list(tail)))[0]
        ind = d[a].pop()

        l[ind] = a
        print(''.join(l))

        ind = tail.index(a)
        f(tail[:ind], tail[ind+1:])
        f(head, "")

a = sorted(set(list(s)))[0]
ind = s.index(a)
f(s[:ind], s[ind:])
