n, m = input().split()
num = 0
for i in range(len(n)):
    m = int(m)
    try:
        num += int(n[len(n) - 1 - i]) * (m ** i)
    except:
        num += (ord(n[len(n) - 1 - i]) - 55) * (m ** i)

print(num)
