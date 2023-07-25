N = int(input())
raw = input()
word = raw.split('*')

for _ in range(N):
    w = input()
    if len(w) < len(raw) - 1: print('NE')
    else:
        if w[:len(word[0])] + '*' + ''.join(reversed(w[::-1][:len(word[1])])) == raw:
            print('DA')
        else: print('NE')
