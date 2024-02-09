import re
for _ in range(int(input())):
 print('YES'if re.compile('^(100+1+|01)+$').match(input())else'NO')
