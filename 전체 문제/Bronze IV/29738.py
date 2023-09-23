for t in range(int(input())):
    n = int(input())
    r = 'Round 1'
    if n <= 25: r = 'World Finals'
    elif n <= 1000: r = 'Round 3'
    elif n <= 4500: r = 'Round 2'
    print(f'Case #{t+1}: {r}')
