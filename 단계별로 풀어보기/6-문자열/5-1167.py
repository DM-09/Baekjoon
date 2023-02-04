word = input().upper()
s = {}
m = ''

for i in range(len(word)):
    if word[i] in s.keys():
        s[word[i]] += 1
    else:
        s[word[i]] = 1

kl = list(s.keys())
vl = list(s.values())

m = max(vl)
max_count = vl.count(m)
if max_count > 1:
    print('?')
else:
    print(kl[vl.index(m)])
