i=input
for _ in range(int(i())):
 s=i()
 r=len(s)-3
 if'MOO'in s:r
 elif'MOM'in s or'OOO'in s:r+=1
 elif'OOM'in s:r+=2
 else:r=-1
 print(r)
