import sys
input = sys.stdin.readline
num = int(input())

total_sum = 0
total_xor = 0

for _ in range(num):
    i = list(map(int, input().split()))
    if i[0] == 1:
        total_sum += i[1]
        total_xor = total_xor ^ i[1]
      
    elif i[0] == 2:
        total_sum -= i[1]
        total_xor = total_xor ^ i[1]
      
    elif i[0] == 3:
        print(total_sum)

    else:
        print(total_xor)
