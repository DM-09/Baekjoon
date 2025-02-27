n, m = map(int, input().split())
tmp = int(1440 * m / n)
print(f'{str(tmp // 60).zfill(2)}:{str(tmp % 60).zfill(2)}')
