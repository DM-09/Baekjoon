le = ['U', 'C', 'P','C']
ind = 0

def chrin(c):
    global ind
    if c == le[ind]:
        ind += 1
        if ind == 4: return 'a'

word = input()

for i in word:
    a = chrin(i)
    if a == 'a':
        print('I love UCPC')
        break
else:
    print('I hate UCPC')
