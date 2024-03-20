ans = 0
papers = [int(input()) for _ in range(6)]
ans += papers[-1]

for i in range(papers[4]): ans += 1; papers[0] -= 11
for j in range(papers[3]):
  ans += 1
  if papers[1] > 4: papers[1] -= 5
  else:
    papers[0] -= 20 - (papers[1] * 4)
    papers[1] = 0

while papers[2] > 0:
  ans += 1
  if papers[2] < 4:
    if papers[2] == 1:
      if papers[1] < 6:
        papers[0] -= 36 - (papers[2] * 9) - (papers[1] * 4)
        papers[1] = 0
      else: papers[1] -= 4; papers[0] -= 11
    elif papers[2] == 2:
      if papers[1] < 3:
        papers[0] -= 36 - (papers[2] * 9) - (papers[1] * 4)
        papers[1] = 0
      else: papers[1] -= 3; papers[0] -= 6
    else:
      if papers[1] < 1:
        papers[0] -= 36 - (papers[2] * 9) - (papers[1] * 4)
        papers[1] = 0
      else: papers[1] -= 1; papers[2] -= 5
    papers[2] = 0
  else: papers[2] -= 4

while papers[1] > 0:
  ans += 1
  a = papers[1]
  if a > 10: a = 9
  papers[1] -= a
  papers[0] -= 36 - (a * 4)

while papers[0] > 0: ans += 1; papers[0] -= 36
print(ans)
