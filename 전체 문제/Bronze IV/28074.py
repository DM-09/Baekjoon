l = ['M', 'O', 'B', 'I', 'S']
k = 0
inp = input()

for i in l:
    if inp.find(i) != -1:
        k += 1
if k == 5:
    print('YES')
else:
    print('NO')
