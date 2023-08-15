import sys
s = ['bowling', 'soccer']
n = int(input())

print(' '.join(['swimming'] * n))
sys.stdout.flush()

def copy(l): return list(l)
st = []

for i in input().split():
    l = copy(s)
    l.remove(i)
    st.append(l[0])

print(' '.join(st))
sys.stdout.flush()
