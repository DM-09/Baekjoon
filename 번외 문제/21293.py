z,y,x,w,v,u,t,s,r,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a = map(int, input().split())

print(a-b)
print(a*b)
print(a+b+1)

'''
해설: 아무거나 제출하고 소스코드를 보면 '다섯 개의 조각을 모아 문제를 완성하자!' 라는 메시지가 나온다. 
이는 백준에서 낼 수 있는 모든 에러를 내면 된다는 것이다.
각 에러마다 힌트가 적혀져 있다.

메모리 초과: 첫 번째 줄에 정수 z,y,x,w,v,u,t,s,r,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a가 주어진다.
출력 초과: 1 ≤ a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,v,w,x,y,z ≤ 10
런타임 에러: 첫 번째 줄에 a-b를 출력한다.
컴파일 에러: 두 번째 줄에 a*b를 출력한다.
시간 초과: 세 번째 줄에 a+b+1을 출력한다.

즉, z,y,x,w,v,u,t,s,r,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a의 입력을 받아
a-b, a*b, a+b+1을 한 줄 씩 출력하면 된다.


여담으로 맞은 소스코드를 보면


예제 입력 1
5 2 9 5 1 9 5 10 9 1 5 4 4 10 1 7 3 5 2 4 3 8 7 3 7

예제 출력 1
4
21
11

이라는 메시지가 있다.
'''


'''
[에러 코드들]

--메모리 초과
a = []
while True:
    a.append(0)


--출력 초과
while True:
    print()
    

--런타임 에러
import time
time.sleep(109990000)


--컴파일 에러
print[]


--시간 초과
for i in range(1000000000):
   for e in range(100000000):
     pass
'''
