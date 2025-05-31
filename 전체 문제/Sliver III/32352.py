a = list(map(int, input().split()))
t = list(map(int, input().split()))

def compare(q, w, e, r):
  return  e<q<r or e<w<r or (e==q and w==r) or q<e<w or q<r<w

h = 0
for i in range(2): h += compare(a[i*2], a[i*2+1], t[i*2], t[i*2+1])

if h < 2: exit(print(-1))
print(min(*a[-2:])-max(*t[-2:])+1)
