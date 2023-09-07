import re

r, c = map(int, input().split())
m = [input() for _ in range(r)]
words = []

def getData(s): return re.sub("#+", '#', s).split('#')

for i in m:
    for j in getData(i):
        if len(j) > 1: words.append(j)

for i in range(c):
    s = ""
    for j in range(r): s += m[j][i]

    for j in getData(s):
        if len(j) > 1: words.append(j)

print(sorted(words))
