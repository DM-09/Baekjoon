import re
n = 0

for i in range(int(input())):
    s = re.sub('1|2|3|5|6|8|9|0', '!', str(i + 1))
    if s.find('!') == -1 and i + 1 > n: n = i + 1

print(n)
