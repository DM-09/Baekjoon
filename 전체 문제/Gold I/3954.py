def move_pointer(sm, ptr, mode=1):
  ptr += 1 if mode else -1
  return ptr % sm


for t in range(int(input())):
  sm, sc, si = map(int, input().split())
  s = input()
  inp = input()

  memory = [0 for i in range(sm)]
  pointer = 0
  inp_num = 0
  loop_list = {}
  l = []

  for i in range(sc):
    c = s[i]
    if c == '[':
      l.append(i)
    elif c == ']':
      tmp = l.pop()
      loop_list[tmp] = i
      loop_list[i] = tmp

  ind = 0
  loop_int = 0
  loop_session = []
  loop_start = sc
  flag = 1

  while ind < sc:
    loop_int += 1
    i = s[ind]
    if i == '+':
      memory[pointer] = (memory[pointer] + 1) % 256
    elif i == '-':
      memory[pointer] = (memory[pointer] - 1) % 256
    elif i == '<':
      pointer = move_pointer(sm, pointer)
    elif i == '>':
      pointer = move_pointer(sm, pointer, 0)
    elif i == '.':
      pass
    elif i == ',':
      if inp_num < si:
        memory[pointer] = ord(inp[inp_num])
        inp_num += 1
      else:
        memory[pointer] = 255
    elif i == '[':
      if memory[pointer] == 0: ind = loop_list[ind]
    elif i == ']':
      if memory[pointer] != 0: ind = loop_list[ind]

    if loop_int > 50000000: loop_start = min(loop_start, ind)
    if loop_int > 2 * 50000000:
      print(f'Loops {loop_start} {loop_list[loop_start]}')
      flag = 0
      break
    ind += 1

  if flag: print('Terminates')
