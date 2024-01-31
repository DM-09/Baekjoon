import re
print('SUBMARINE'if re.compile('^(100+1+|01)+$').match(input())else'NOISE')
