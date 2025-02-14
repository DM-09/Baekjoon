n = int(input())
s = 'long long'
if -pow(2,15) <= n <= pow(2,15)-1: s = 'short'
elif -pow(2,31) <= n <= pow(2,31)-1: s = 'int'
print(s)
