n = int(input())
i, j = 0, 0

while True:
    i += 1
    if str(i).find('666') != -1:
        j += 1
    if j == n:
        print(i)
        break
