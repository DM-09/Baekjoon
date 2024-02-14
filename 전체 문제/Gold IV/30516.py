I=input
P=print
L=len
n=int(I())
a=list(map(int,I().split()))
l=[]
g=[]
b=p=0
for i in a:
 if i!=0and p==i:l+=[g];g=[]
 g+=[i];p=i
l+=[g]
if n==2and a[0]==a[1]!=0:print(-1);exit()
if L(l)==2and l[0][0]==l[1][-1]!=0:q=l.pop();l.extend([[q[0]],q[1:]])
P(L(l))
P(*[L(i)for i in l])
P(*range(L(l),0,-1))
