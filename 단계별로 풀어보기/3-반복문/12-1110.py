num_o = input()
rep = 0

if int(num_o) < 10:
    num_o = '0' + num_o

num = num_o[0] + num_o[1]

while True:
    num_box = [int(num[0]), int(num[1])]
    sums = str(sum(num_box))

    left = num_box[len(num_box) - 1]
    right = str(sums)[len(sums) - 1]

    num = str(left) + right

    if num == num_o:
        print(rep + 1)
        break
    else:
        rep = rep + 1
