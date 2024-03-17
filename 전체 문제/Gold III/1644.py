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
 return b

n = int(input())
l = Linear_Sieve(4000000)
ans = 0
Sum = 0
end = 0

all = len(l)

for start in range(n):
  while end < all and Sum < n:
    Sum += l[end]
    end += 1
  if Sum == n: ans += 1
  if start >= all: break
  Sum -= l[start]

print(ans)
