l = {'@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n', '0': 'o', '7': 't',
     "\\\\'": 'w', "\\'": 'v'}


for _ in range(int(input())):
    word, wl = input(), 0
    new = word

    for i in l.items():
        wl += new.count(i[0])
        new = new.replace(i[0], i[1])

    if len(new) / 2 <= wl: print("I don't understand")
    else: print(new)
