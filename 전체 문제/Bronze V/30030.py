n = int(input())

for i in range(1000, 9900):
   if i + i // 10 == n: print(i); break
