p = set()
p.add(" ")

for i in range(int(input())):
  raw_s = input()
  s = raw_s.split()
  flag = True
  # 1 전략
  for index, word in enumerate(s):
    if not word[0].upper() in p:
      p.add(word[0].upper())
      word = list(word)
      st = f"[{word[0]}]{''.join(word[1:])}"
      s[index] = st
      break
  else:
    # 2 전략
    for index, alphabet in enumerate(raw_s):
      if not alphabet.upper() in p:
        p.add(alphabet.upper())
        print(f"{raw_s[:index]}[{raw_s[index]}]{raw_s[index+1:]}")
        flag = False
        break
  if flag: print(*s)
