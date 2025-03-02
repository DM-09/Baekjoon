from collections import defaultdict as dd
import sys
input = sys.stdin.readline

def Sieve(M):
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

n = int(input())
facl = Sieve(10**6)
pele = dd(int)
r = 1
p = dd(int)

for _ in range(n):
 a = int(input())
 q = set()

 if a == 1: print(['NE','DA'][r]); continue
 while a > 1:
  b = facl[a]
  if pele[b]: del p[b]
  else: p[b] = 1
  pele[b] = +(not pele[b])
  q.add(b)
  a //= b
 r = len(p) == 0
 print(['NE','DA'][r])
