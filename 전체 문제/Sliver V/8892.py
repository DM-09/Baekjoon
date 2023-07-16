def isPalindrome(w):
    if w == w[::-1]:
        return True
    return False


for _ in range(int(input())):
    words = [input() for _ in range(int(input()))]
    lw, Flag = len(words), True

    for i in range(lw):
        for j in range(lw):
            if i != j:
                word = words[i] + words[j]
                if isPalindrome(word):
                    Flag = False
                    print(word)
                    break
        if not Flag: break
    if Flag: print(0)
