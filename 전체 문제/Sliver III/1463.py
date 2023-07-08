num = int(input())

result = [0 for i in range(num + 1)]
result[0] = 999999


for i in range(2, num + 1):
  two, three = i // 2, i // 3
  if i % 2 != 0:
    two = 0
  if i % 3 != 0:
    three = 0
    
  result[i] = min(result[i-1] + 1, result[two] + 1, result[three] + 1)
print(result[num])
