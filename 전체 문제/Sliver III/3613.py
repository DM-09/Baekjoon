import re
word = input()
new = ''

new = word
word = re.sub('A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z', '~', word)

if new[0].isupper() or new[0] == '_' or new.find('__') != -1 or new[len(new) - 1] == '_':
    print('Error!')
elif word.find('~') != -1 and word.find('_') != -1:
    print('Error!')
elif word.find('_') != -1:
    # C++
    word = new
    word = word.split('_')
    new = ''
    for i in range(len(word)):
        if i != 0:
            wi = word[i]
            word[i] = wi[0].upper() + wi[1:]
        new += word[i]
    print(new)
elif word.find('~') != -1:
    # Java
    for i in range(word.count('~')):
        index = word.index('~') - i
        word = word.replace('~', '_' + new[index].lower(), 1)
    print(word)
else:
    print(new)
