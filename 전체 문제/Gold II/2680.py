an ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'

for _ in range(int(input())):
  s = ''.join(bin(int(i,16))[2:].zfill(4) for i in input())
  i, c, r = 0, 0, []

  while i < len(s):
    code = s[i:i+4]
    i += 4

    if code == '0001':
      cnt = int(s[i:i+10], 2)
      i += 10
      while cnt:
        if cnt >= 3:
          r.append(str(int(s[i:i+10], 2)).zfill(3))
          cnt -= 3; c += 3; i += 10
        elif cnt == 2:
          r.append(str(int(s[i:i+7], 2)).zfill(2))
          cnt -= 2; c += 2; i += 7
        elif cnt == 1:
          r.append(str(int(s[i:i+4], 2)))
          cnt -= 1; c += 1; i += 4

    elif code == '0010':
      cnt = int(s[i:i+9], 2)
      i += 9
      while cnt:
        if cnt >= 2:
          tmp = int(s[i:i+11], 2)
          r.append(an[tmp//45]+an[tmp%45])
          i += 11; c += 2; cnt -= 2
        elif cnt == 1:
          r.append(an[int(s[i:i+6], 2)])
          i += 6; c += 1; cnt -= 1

    elif code == '0100':
      cnt = int(s[i:i+8], 2)
      i += 8
      for _ in range(cnt):
        a = int(s[i:i+8], 2)
        if a == 0x20: r.append(' ')
        elif a == 0x23: r.append('\\#')
        elif a == 0x5c: r.append('\\\\')
        elif 0x20 <= a <= 0x7e: r.append(chr(a))
        else: r.append('\\'+hex(a)[2:].upper().zfill(2))
        i += 8; c += 1

    elif code == '1000':
      cnt = int(s[i:i+8], 2)
      i += 8
      for _ in range(cnt):
        r.append('#'+hex(int(s[i:i+13], 2))[2:].upper().zfill(4))
        c += 1; i += 13

    else: break
  print(c, ''.join(r))
