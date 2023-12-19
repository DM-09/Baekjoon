import sys
input = sys.stdin.readline

s = input()
box = [([0] * (len(s) + 1)) for _ in range(26)]

for a in range(97, 123):
    for i in range(len(s)):
        box[a-97][i + 1] = box[a-97][i] + (1 if s[i] == chr(a) else 0)


for q in range(int(input())):
    a, l, r = input().split()
    l, r = int(l), int(r)

    print(box[ord(a)-97][r + 1] - box[ord(a)-97][l])
