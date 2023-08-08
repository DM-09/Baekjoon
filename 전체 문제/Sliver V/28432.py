start, end = '', ''
log = [input() for _ in range(int(input()))]

q_ind = log.index('?')

try: start = log[q_ind - 1 if (q_ind - 1) > 0 else 0][-1]
except: pass

try: end = log[q_ind + 1][0]
except: pass

if start == '?': start = ''
if end == '?': end = ''

for _ in range(int(input())):
    i = input()

    if start == '' or i[0] == start:
        if end == '' or i[-1] == end:
            if not i in log: print(i)
