q1, q2, q3, q4, ax = 0, 0, 0, 0, 0

for _ in range(int(input())):
    a, b = map(int, input().split())
   
    if a == 0 or b == 0: ax += 1
    elif a > 0 and b > 0: q1 += 1
    elif a < 0 and b > 0: q2 += 1
    elif a < 0 and b < 0: q3 += 1
    elif a > 0 and b < 0: q4 += 1
print(f'''Q1: {q1}
Q2: {q2}
Q3: {q3}
Q4: {q4}
AXIS: {ax}''')
