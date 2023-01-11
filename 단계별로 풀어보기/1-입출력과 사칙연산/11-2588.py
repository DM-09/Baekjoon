a = int(input())
b = input()

t = int(b[2]) * a, int(b[1]) * a, int(b[0]) * a
print(t[0])
print(t[1])
print(t[2])

sum_result = 0
for i in range(3):
    sum_result += int(t[i] * 10 ** i)

print(sum_result)
