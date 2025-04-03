# 입력: UR, TR, UO, TO
UR, TR, UO, TO = map(int, input().split())

# 점수 계산
score = 56 * UR + 24 * TR + 14 * UO + 6 * TO

# 출력
print(score)
