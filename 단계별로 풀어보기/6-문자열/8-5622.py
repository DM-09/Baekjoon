al = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXZY']
word = input().upper()
seconds = 0

for char in word:
    for index in range(len(al)):
        if char in al[index]:
            seconds += index + 3
            break

print(seconds)
