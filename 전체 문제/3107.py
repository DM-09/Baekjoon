inp = input()
rep = inp.replace('::', ':!:')
ip = rep.split(':')
new = []
IP = ''

for i in range(len(ip)):
    if ip[i] == '!':
        for c in range(8 - len(ip) + 1):
            new.append('0000')
    else:
        char = '0' * (4 - len(ip[i])) + ip[i]
        new.append(char)

for ch in range(len(new)):
    IP += new[ch]
    if ch != len(new) - 1:
        IP += ':'

print(IP)
