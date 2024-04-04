c = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
j = ' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'
tmp = ord(input()) - 44032

cho = c[tmp // 588]
jng = chr(12623 + tmp % 588 // 28)
jong = j[tmp % 588 % 28]

print(cho, jng, jong)
