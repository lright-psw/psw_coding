import sys

input = sys.stdin.readline


def clacd_sum(tree, hight):
    total = 0
    for t in tree:
        if t > hight:
            total += t - hight
    return total


def main():
    N, M = map(int, input().strip().split())
    tree = list(map(int, input().strip().split()))

    low = 0
    high = max(tree)
    rst = 0

    while low <= high:
        mid = (low + high) // 2
        sum = clacd_sum(tree, mid)

        # 0 ------- 중간 ------- high
        # 만약 더 크면 중간부터 high까지 다시 검색
        # 만약 더 작으면 0-중간까지 비교교
        if sum >= M:
            rst = mid
            low = mid + 1
        else:
            high = mid - 1

    print(rst)


if __name__ == "__main__":
    main()
