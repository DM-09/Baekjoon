import sys
input = sys.stdin.readline

n = input()
v = 0
f = 0

log, a, pre = [], [], ''

for c in input():
    if c in 'SMUPC':
        num = int(''.join(a))
        a = ["0"]
        if num or f:
            if pre == "": v = num
            elif pre == "S": v -= num
            elif pre == "M": v *= num
            elif pre == "U":
                if v < 0: v = (-v // num) * -1
                else: v = v // num
            elif pre == "P": v += num

        f = 0
        pre = c
        if c == 'C': log.append(v); pre = "-"
    else:
        a.append(c)
        f = 1

if log: print(*log)
else: print("NO OUTPUT")
