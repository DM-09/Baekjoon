n = int(input())

ext_dict = dict()

for _ in range(n):
  word, extension = input().split(".")
  if not extension in ext_dict:
    ext_dict[extension] = 1
  else:
    ext_dict[extension] += 1

sorted_ext_dict = sorted(ext_dict.items())

for key, value in sorted_ext_dict:
  print(key, value)
