n = int(input())
s = input()
ans = 0

newS = ''
pre = ''
for i in s:
  if i != pre: newS += i
  pre = i

a = 'RB'[+newS.count('B') > newS.count('R')]

pre = ''
for i in s:
  if i != a  and i != pre: ans += 1
  pre = i

print(ans + 1)
