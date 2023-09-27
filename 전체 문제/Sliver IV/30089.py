t = int(input().strip())

for _ in range(t):
    s = input().strip()

    if s[::-1] == s:
        print(s[::-1])
    else:
        l = []
        p = [s + s[::-1][1:], s + s[0]]

        for i in range(len(s)):
            n = s + s[::-1][i:]
            if n[:len(s)] == s and n[::-1][:len(s)] == s: p.append(n)

        for i in p:
            if i[:len(s)] == s and i[::-1][:len(s)] == s: l.append(i)
        print(min(l, key=len))
