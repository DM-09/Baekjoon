cal = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
num = 0
i = 0
while i < len(word):
    if word[i] == 'c':
        if i + 1 < len(word):
            if word[i + 1] in ['=', '-']:
                i += 1

    elif word[i] == 'd':
        if i + 1 < len(word):
            if word[i + 1] == 'z':
                if i + 2 < len(word):
                    if word[i + 2] == '=':
                        i += 2

            elif word[i + 1] == '-':
                i += 1

    elif word[i] == 'l':
        if i + 1 < len(word):
            if word[i + 1] == 'j':
                i += 1

    elif word[i] == 'n':
        if i + 1 < len(word):
            if word[i + 1] == 'j':
                i += 1

    elif word[i] == 's':
        if i + 1 < len(word):
            if word[i + 1] == '=':
                i += 1

    elif word[i] == 'z':
        if i + 1 < len(word):
            if word[i + 1] == '=':
                i += 1

    num += 1
    i += 1

print(num)
