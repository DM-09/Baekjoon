import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
max_honey = 0

box = []
box.append(l[0])

for i in range(1, n):
    box.append(box[i-1]+l[i])
    
for i in range(1, n-1):
    max_honey = max(max_honey, (box[n-1] - l[0]) - l[i] + (box[n-1] - box[i]))
    
for i in range(1, n-1):
  max_honey = max(max_honey, box[n-2] - l[i] + box[i-1])

for i in range(1, n-1):
  max_honey = max(max_honey, box[n-2] - l[0] + l[i])

print(max_honey)
