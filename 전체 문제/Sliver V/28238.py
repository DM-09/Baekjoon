student_max = int(input())
student_list = []
for i in range(student_max):
  l = list(map(int, input().split()))
  student_list.append(l)

best_first, best_second = 0, 1
best_couple_score = 0

for first in range(0, 5):
  for second in range(first + 1, 5):
    count = 0
    for student in student_list:
      if student[first] == 1 and student[second] == 1:
        count += 1
    if count > best_couple_score:
      best_couple_score = count
      best_first, best_second = first, second

print(best_couple_score)

l = [0, 0, 0, 0, 0]
l[best_first] = 1
l[best_second] = 1

print(*l)
