from itertools import permutations

N, M = map(int, input().split())
nums = [i + 1 for i in range(N)]

for i in permutations(nums, M):
    print(*list(i))
