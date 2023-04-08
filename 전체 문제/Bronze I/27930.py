import copy

inp = input()
l = [['Y', 'O', 'N', 'S', 'E', 'I'], ['K', 'O', 'R', 'E', 'A']]
original_uni = copy.deepcopy(l)

for i in inp:
    for list_index in range(len(l)):
        if l[list_index]:
            if i == l[list_index][0]:
                del l[list_index][0]
                if not l[list_index]:
                    print(''.join(original_uni[list_index]))
                    exit()
