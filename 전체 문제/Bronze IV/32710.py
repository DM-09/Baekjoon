n=int(input())
for i in range(2,10):
 for j in range(1,10):
  if n in [i,j,i*j]: exit(print(1))
print(0)
