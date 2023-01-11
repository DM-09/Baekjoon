List = []
n = 1

for i in range(10000):  # 리스트 자동 돌리기
    List.append(i + 1)

while True:
    nn = n  # 생성자

    for digit in str(n):
        nn += int(digit)

    if n > 10000:  # 만약 생성자 가 만을 넘으면
        for p in range(len(List)):  # 리스트 에 남아 있는 것들을 출력
            print(List[p])
        break  # 멈추기

    try:
        List.remove(nn)  # 리스트 에서 생성자 수 삭제
    except ValueError:
        pass

    n += 1  # n에 1 추가
