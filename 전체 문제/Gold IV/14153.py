n=int(input())
s=['/\\','/__\\']
b=2**n-1
t=1
d='.'
while t<n:
 a=len(s[-1])
 for i in s[:]:s.append(i+d*a+i)
 t+=1
for i in s:print(d*b+i);b-=1
