S = input()
re = ''
en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
      'w', 'x', 'y', 'z']

for i in range(len(en)):
    re += str(S.find(en[i])) + ' '

print(re)
