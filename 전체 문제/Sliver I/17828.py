n, x = map(int, input().split())
num_of_Z = (x - n) // 25
if not n <= x <= n*26: exit(print('!'))
l = ['A'] * (n - num_of_Z - 1)
l.append(chr(x - (num_of_Z * 26) - len(l) + 64))
l.extend(['Z'] * num_of_Z)
if n == num_of_Z: exit(print('Z'*n))
print(''.join(l))
