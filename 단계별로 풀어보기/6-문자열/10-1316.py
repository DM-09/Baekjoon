N = int(input())
num = 0

for i in range(N):
    word = input()
    char = '' 

    for c in range(len(word) - 1):
        char += word[c]
        if word[c + 1] in char and char[-1] != word[c + 1]:
            break
    else:
        num += 1 

print(num)
