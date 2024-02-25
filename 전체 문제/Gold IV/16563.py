def Linear_Sieve(M):
 N=M+1
 l=[0]*(N)
 b=[]
 for i in range(2,N):
  if l[i]==0:b.append(i);l[i]=i
  for p in b:
   x = i * p
   if x > M: break
   l[x] = p
   if i % p == 0: break
 return l

l = Linear_Sieve(5000000)
n = int(input())
def div(n):
  global l
  a = []
  while n > 1:
    x = l[n]
    n //= x
    a.append(x)
  return a

for i in list(map(int, input().split())): print(*div(i))
