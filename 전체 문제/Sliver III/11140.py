def lol_maker(s : str):
    if 'lol' in s: return 0
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if 'l' + i + 'l' in s: return 1
    if 'lo' in s or 'ol' in s or 'll' in s: return 1
    if 'l' in s or 'o' in s: return 2

    return 3

for _ in range(int(input())): print(lol_maker(input()))
