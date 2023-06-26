word = input()
n = 0

for i in range(int(input())):
    inp = input()
    if (inp + inp).find(word) != -1:
        n += 1
print(n)
