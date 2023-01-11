import math

l = []  # blank list

for i in range(10):  # intput
    inp = input()
    l.append(math.floor(int(inp) % 42))  # add result

new_l = len(set(l))  # set

print(new_l)  # print
