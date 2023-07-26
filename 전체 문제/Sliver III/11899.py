s = input()

for _ in range(25): s = s.replace('()', '')
print(len(s))
