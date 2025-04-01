A = 0
for i in range(1,9):
 inp = input()
 for j in range(8):
  if ((i%2 and (j+1)%2) or (i%2==0 and (j+1)%2==0)) and inp[j] == 'F':
   A += 1
print(A)
