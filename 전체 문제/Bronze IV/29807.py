t = int(input().strip())
s = list(map(int, input().strip().split())) + ([0] * (5 - t))
l, n = [abs(s[0] - s[2]), abs(s[1] - s[3])], 0

n += 508 * l[0] if s[0] > s[2] else 108 * l[0]
n += 212 * l[1] if s[1] > s[3] else 305 * l[1]
n += 707 * s[4]

print(n * 4763)
