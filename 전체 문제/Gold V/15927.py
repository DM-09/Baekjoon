a=len(s:=input())
if s==s[::-1]:a-=1
print(a if len(set(s))!=1 else-1)
