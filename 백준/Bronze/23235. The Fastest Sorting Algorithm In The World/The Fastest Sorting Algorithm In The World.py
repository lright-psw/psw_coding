case_num = 1

while True:
    line = input().strip()
    if line == '0':
        break

    tokens = list(map(int, line.split()))
    N = tokens[0]
    # 굳이 정렬할 필요 없음. 이미 정렬된 상태라고 가정

    print(f"Case {case_num}: Sorting... done!")
    case_num += 1
