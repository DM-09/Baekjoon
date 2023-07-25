while True:
    raw = input()
    a = list(raw.replace('.', '').split(', '))

    if raw == '.': break

    nums, strs = [], []

    for i in range(len(a)):
        e = a[i]
        e_type = 'str'

        if e.replace('-', '').isdigit(): nums.append(int(e)); e_type = ''
        else: strs.append(e)

        a[i] = e_type

    nums.sort(); strs.sort(key=lambda x: str(x).lower())

    for i in range(len(a)):
        e = a[i]

        if e == 'str': a[i] = strs.pop(0)
        else: a[i] = str(nums.pop(0))

    print(', '.join(a) + '.')
