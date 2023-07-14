word = input()
flag, tag_str, st = False, '', ''

def re(w):
    l = []
    for i in w.split(' '):
        l.append(''.join(reversed(i)))
    return l

if word.count('<') == 0:
    print(' '.join(re(word)))
else:
    for i in word:
        if i == '<':
            print(' '.join(re(st)), end='')
            flag, st = True, ''

        if flag: tag_str += i
        else: st += i

        if i == '>':
            print(tag_str, end='')
            flag, tag_str = False, ''

print(' '.join(re(st)), end='')
