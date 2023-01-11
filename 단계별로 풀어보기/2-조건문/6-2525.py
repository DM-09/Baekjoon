import math  # math 임포트

a, b = input().split()  # a = 시 , b = 분
a, b = int(a), int(b)  # a, b int 로

c = int(input())  # c = 조리 시간

added = (a * 60) + b + c  # 현재 시각을 분으로 바꾼다. 추가로 조리 시간을 더한다.

H = math.floor(added / 60)  # 시 = 더한거 에서 시간(60분)으로 나눔
M = added % 60  # 분 = 더한거 에서 시간(60분)으로 나눈 나머지

if H >= 24:  # 만약 시 가 24시간을 넘겼 다면
    H = H - 24  # 다음 날로 넘어 가기 때문에 24시간(하루)를 빼준다.

print(H, M) # 최종 결과 출력
