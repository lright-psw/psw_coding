T = int(input())

for _ in range(T):
    # 현재 테스트 케이스의 쿠키 상자 입력
    box = list(input())

    # 만들고 싶은 단어 수
    W = int(input())

    for _ in range(W):
        word = input()
        temp = box.copy()  # 원본 보존용 복사본
        flag = True

        for ch in word:
            if ch in temp:
                temp.remove(ch)  # 사용한 글자 제거
            else:
                flag = False
                break

        print("YES" if flag else "NO")
