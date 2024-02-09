I=input
n=int(I())
l=set([I()for _ in'0'*n])
a=0
for i in l:
 for j in l:
  if i!=j and i==j[:len(i)]:a+=1;break
print(len(l)-a)
