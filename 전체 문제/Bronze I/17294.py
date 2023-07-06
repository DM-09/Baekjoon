k = input()

if len(k) in [1, 2] or len(set(k)) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    d = int(k[0]) - int(k[1])

    for i in range(1, len(k) - 1):
        if int(k[i]) - int(k[i+1]) != d:
            print('흥칫뿡!! <(￣ ﹌ ￣)>')
            break
    else:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
