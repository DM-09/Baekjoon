a=divmod(int(input())*7+1,12)
print(*[2024+a[0],a[1]]if a[1]else[2024+a[0]-1,12])
