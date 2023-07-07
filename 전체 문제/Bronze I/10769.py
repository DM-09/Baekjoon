s = input()
ha, sa = s.count(':-)'), s.count(':-(')

if ha + sa == 0:
    print('none')
elif ha == sa:
    print('unsure')
elif ha > sa:
    print('happy')
else:
    print('sad')
