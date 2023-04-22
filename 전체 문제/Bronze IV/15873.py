i = input().replace('10', ' 10 ').split()

if len(i) == 2:
    print(int(i[0]) + int(i[1]))
else:
    print(int(i[0][0]) + int(i[0][1]))
