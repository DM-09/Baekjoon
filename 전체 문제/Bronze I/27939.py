N = int(input())
egg_plant = input().split()
m, k = map(int, input().split())

for i in range(m):
    h = list(map(int, input().split()))
    for e in range(len(h)):
        if egg_plant[h[e] - 1] == 'P': break
    else:
        print('W')
        break
else:
    print('P')
