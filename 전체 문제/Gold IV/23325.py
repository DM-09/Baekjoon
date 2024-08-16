c={'+-':1,'++':10,'++-':11,'--':-1,'-+':-10,'-+-':-11}
p=f'+{input()} '
l=len(p)-2
f=-1000000
d=[f]*(l+2)
d[0]=0
for i in range(l):
 b=d[i]
 q,w=p[i:i+2],p[i:i+3]
 if b!=f:
  if q in c and d[i+2]<(r:=c[q]+b):d[i+2]=r
  if w in c and d[i+3]<(r:=c[w]+b):d[i+3]=r
print(d[-1])
