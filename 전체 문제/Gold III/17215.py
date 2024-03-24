s=input()
l=[]
a=b=c=d=0
f=len
for i in range(f(s)):
 q=s[i];n=0
 if q=='S':n=10;d+=1
 elif q=='P':n=10-c
 elif q!='-':n=int(q)
 if(i+d)%2:a+=1
 b+=n;c=n
 for _ in l:
  if l.pop()=='S':l+=[n]
  b+=n
 if a<10and q in'SP':l+=[q]
print(b)
