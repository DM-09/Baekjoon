i, j = input(), 0

for _ in range(len(i)):
    if j > len(i):
        break
        
    print(i[j : j + 10])
    
    j += 10
    if j >= len(i):
        j = len(i)
