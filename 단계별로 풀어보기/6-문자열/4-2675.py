T = input()

for i in range(int(T)):
    S = input().split()
    Str = ''
    for char in S[1]:
        for e in range(int(S[0])):
            Str += char
    print(Str)
