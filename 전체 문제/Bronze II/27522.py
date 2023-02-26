Record = []
Score = [10, 8, 6, 5, 4, 3, 2, 1]
Red = 0
Blue = 0

for i in range(8):
    info = input().split()
    Record.append(info)

Record.sort()

for r in range(8):
    t = Record[r][1]

    if t == 'R':
        Red += Score[r]
    else:
        Blue += Score[r]

if Red > Blue:
    print('Red')
elif Blue > Red:
    print('Blue')
else:
    m = min(Record)[1]
    if m == 'B':
        print('Blue')
    else:
        print('Red')
