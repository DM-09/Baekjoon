import re

n = int(input())

for a in range(n):
    s1, s2 = input().lower(), input().lower()

    ori = ['\(|\[|\{', '\)|\]|\}', ',|;', '\.', ':' ,'  *']
    rep = [' ( ', ' ) ', ' ; ', ' . ', ' : ', ' ']

    for i in range(6):
        s1 = re.sub(ori[i], rep[i], s1)
        s2 = re.sub(ori[i], rep[i], s2)

    print(f'Data Set {a + 1}: ' + ('equal' if s1 == s2 else 'not equal'))
    if a != n: print()
