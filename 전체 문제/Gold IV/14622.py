I=input
a=b=0
q=[]
w=[]
d={}
t=1000
def S(n):
 if n in[0,1]:return 0
 for i in range(2,int(n**.5)+1):
  if n%i==0:return 0
 return 1
for _ in' '*int(I()):
 x,y= map(int,I().split())
 if S(x):
  if x in d:a-=t
  else:d[x]=1;q.append(x);q.sort()
 else:
  if len(w)<3:b+=t
  else:b+=w[-3]
 if S(y):
  if y in d:b-=t
  else:d[y]=1;w.append(y);w.sort()
 else:
  if len(q)<3:a+=t
  else:a+=q[-3]
p='우열을 가릴 수 없음'
if a<b:p='소수 마스터 갓규성'
if a>b:p='소수의 신 갓대웅'
print(p)
