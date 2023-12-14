s=''
while 1:
 try:i=input().split()
 except:
  if s!='':print(s)
  break
 for a in i:
  if a=='<hr>':
   if s!='':print(s);s=''
   print('-'*80)
  elif a=='<br>':print(s);s=''
  elif s=='':s=a
  elif len(s+a)+1<81:s+=' '+a
  else:print(s);s=a
