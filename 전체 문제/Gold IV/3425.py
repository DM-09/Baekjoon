e='ERROR'
def f(c,n):
 s=[n]
 for i in c:
  a=b=0;m=1
  if i=='POP':
   if s:s.pop();continue
   return e
  elif i=='INV':
   if s:s[-1]*=-1;continue
   return e
  elif i=='DUP':
   if s:s.append(s[-1]);continue
   return e
  elif i[:3]=='NUM':s.append(int(i.split()[1]));continue
  if len(s)<2:return e
  a,b=s.pop(),s.pop()
  if i=='SWP':s.append(a);s.append(b)
  elif i=='ADD':s.append(a+b)
  elif i=='SUB':s.append(b-a)
  elif i=='MUL':s.append(a*b)
  elif i=='DIV':
   if a==0: return e
   s.append(int(b/a))
  elif i=='MOD':
   if a==0: return e
   if b<0:m=-1
   s.append(abs(b)%abs(a)*m)
  if abs(s[-1])>10**9:return e
 if len(s)==1:return s[0]
 return e
I=input
P=print
while 1:
 c=[]
 while 1:
  i=I()
  if i=='QUIT':exit(0)
  if i=='END':break
  if i!='': c.append(i)
 for _ in' '*int(I()):P(f(c,int(I())))
 P()
