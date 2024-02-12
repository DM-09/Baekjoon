from itertools import*
I=input
S=set
P=print
n,k=map(int,I().split())
a=S('antic')
w=[S(I())-a for _ in' '*n]
l=S('bdefghjklmopqrsuvwxyz')
b=0
k-=5
if k<0:P(0);exit()
for i in S(combinations(l,k)):i=S(i);b=max(b,sum(+(i>=j)for j in w))
P(b)
