def bf_compiler(code):
  biteList = [0] * 32768
  pointer = 0
  List = {}
  pre = []
  todo = 1
  output = []

  for i in range(len(code)):
    if code[i] == '[':
      List[i] = -1; pre.append(i)
    elif code[i] == ']':
      if pre: a = pre.pop(); List[a] = i; List[i] = a
      else: return 'COMPILE ERROR'

  for i in List:
    if List[i] == -1: return 'COMPILE ERROR'

  while todo:
    i = code[todo - 1]

    if i == '+':
      value = biteList[pointer]
      update = value + 1
      if value == 255: update = 0
      biteList[pointer] = update
    elif i == '-':
      value = biteList[pointer]
      update = value - 1
      if value == 0: update = 255
      biteList[pointer] = update
    elif i == '>':
      if pointer == 32767: pointer = 0
      else: pointer += 1
    elif i == '<':
      if pointer == 0: pointer = 32767
      else: pointer -= 1
    elif i == '.': output.append(chr(biteList[pointer]))
    elif i == '[' and biteList[pointer] == 0: todo = List[todo - 1]
    elif i == ']' and biteList[pointer]: todo = List[todo - 1]

    if todo == len(code): break
    todo += 1

  return ''.join(output)


for i in range(int(input())):
  code = []
  while 1:
    inp = input()
    if inp == 'end': break
    for j in inp:
      if j == '%': break
      code.append(j)

  print(f'PROGRAM #{i+1}:')
  print(bf_compiler(''.join(code)))
