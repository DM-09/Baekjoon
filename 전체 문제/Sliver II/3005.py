r, c = map(int, input().split())
Map, words = [input() for _ in range(r)], []

def add(w):
    global words
    for i in w.split('#'):
        if len(i) > 1: words.append(i)

for i in Map: add(i)

for i in range(c):
    word = ''
    for j in range(r): word += Map[j][i]

    add(word)

print(sorted(words)[0])
