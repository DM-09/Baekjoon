for _ in range(int(input())):
    n = int(input())
    a = int(str(n)[-2:])
    
    if ((n+1) // a) * a == n+1: print('Good')
    else: print('Bye')
