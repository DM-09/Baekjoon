import itertools as it

rom1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
rom2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = input()
m = 100
s = n

def make_Rom_num(s : str):
    if s.isdigit():
        if len(s) == 1: return rom1[int(s[0])-1]
        return rom2[int(s[0])-1] + rom1[int(s[1])-1]
    else:
        ten=one=''
        mode = 0
        for i in s:
            if i in 'IV': mode = 1
            if mode: one += i
            else: ten += i

        try: a = str(rom2.index(ten) + 1)
        except: a = '0'

        try: b = str(rom1.index(one) + 1)
        except: a, b = '0', '0'

        if ten == '': return int(b)
        elif ten and not int(a): return 0

        return int(a + b)

for i in set(it.permutations(n)):
    if c := make_Rom_num(''.join(i)):
        if c < m: m = c; s = ''.join(i)

print(s)
