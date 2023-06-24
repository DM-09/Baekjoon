N = int(input())
nums = sorted(int(input()) for _ in range(N))

for i in range(1, N):
    if i >= nums[i]:
        print(i + 1)
        break
