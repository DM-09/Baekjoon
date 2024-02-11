from itertools import*
I=input
S=set
n,k=map(int,I().split())
a=S('antic')
w=[S(I())-a for _ in range(n)]
l=S('bdefghjklmopqrsuvwxyz')
b=0
k-=5
if k<0:print(0);exit(0)
for i in S(combinations(l,k)):i=S(i);b=max(b,sum(+(i>=j)for j in w))
print(b)
