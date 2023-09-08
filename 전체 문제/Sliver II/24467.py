n, moved, m = 0, 0, 20

def forward(s):
    global n
    if s == '0000': n -= 1; return 4
    if s == '1111': n -= 1; return 5
    n += 1
    return s.count('0')

while n != 10:
    i = input()
    moved += forward(i)

    if moved > m: print("WIN"); break

    if moved == 5 or moved == 10 and m == 20: m = 16
    if moved == 8 and m == 16: m = 11

else: print("LOSE")
