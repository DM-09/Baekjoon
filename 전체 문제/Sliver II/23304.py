def isAKARAKA(s):
    if len(s) == 1: return ''
    if s == s[::-1]:
        l = len(s) // 2
        head, tail = s[:l], s[len(s) - l:]

        if head == head[::-1] and tail == tail[::-1]:
            return isAKARAKA(head) + isAKARAKA(tail)
    return '1'

print('AKARAKA' if isAKARAKA(input()) == '' else 'IPSELENTI')
