s = ''
for i in range(5):
    if input().find('FBI') != -1:
        s += str(i + 1)

if s == '':
    print('HE GOT AWAY!')
else:
    print(' '.join(s))
