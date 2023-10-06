while 1:
    q, w, e = map(int, input().split())
    if q + w + e == 0: break
    
    m = sorted([q, w, e])
    a, b, c = m[0], m[1], m[2]
    
    if a * a + b * b == c * c:
        print('right')
    else: print('wrong')
