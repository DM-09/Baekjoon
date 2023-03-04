import re
word = input()

word = re.sub('<', ' < ', word)
word = re.sub('>', ' > ', word)
word = re.sub('&&', ' && ', word)
word = re.sub('\|\|', ' || ', word)
word = re.sub('\(', ' ( ', word)
word = re.sub('\)', ' ) ', word)
word = ' '.join(word.split())

print(word)
