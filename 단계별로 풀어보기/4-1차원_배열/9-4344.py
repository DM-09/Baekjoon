c = int(input())  # 케이스 개수

for i in range(c):  # 케이스 만큼 돌림
    inp = input().split()  # 입력

    for d in range(len(inp)):  # 정수로 바꾸기 위한 반복문
        inp[d] = int(inp[d])  # 모두 정수로 바꿔줌
    a_score = (sum(inp) - int(inp[0])) / int(inp[0])  # 평균 점수
    n = 0  # 빈 변수

    for s in range(int(inp[0])):  # N명 만큼 반복
        if inp[s + 1] > a_score:  # 점수가 평균 보다 높으면
            n += 1  # 사람 수를 저장

    result = (n / int(inp[0])) * 100  # 최종 값
    print(f'{result:.3f}%')  # 결과 출력(소수점 까지)
