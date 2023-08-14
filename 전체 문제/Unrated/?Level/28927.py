max = list(map(int, input().split()))
mel = list(map(int, input().split()))

max = max[0] * 3 + max[1] * 20 + max[2] * 120
mel = mel[0] * 3 + mel[1] * 20 + mel[2] * 120

if max > mel: print('Max')
if max < mel: print('Mel')
if max == mel: print('Draw')
