inp = input().split()
A, B = inp[0], inp[1]
As = [int(A.replace('5', '6')), int(A.replace('6', '5'))]
Bs = [int(B.replace('5', '6')), int(B.replace('6', '5'))]

print(min(As) + min(Bs), max(As) + max(Bs))
