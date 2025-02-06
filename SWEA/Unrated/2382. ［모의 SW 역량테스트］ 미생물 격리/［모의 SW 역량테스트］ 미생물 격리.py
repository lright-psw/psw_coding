def simulate_microorganisms(N, M, K, clusters):
    from collections import defaultdict

    # 이동 방향: 상(1), 하(2), 좌(3), 우(4)
    directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    reverse_dir = {1: 2, 2: 1, 3: 4, 4: 3}

    for _ in range(M):
        new_clusters = defaultdict(list)

        # 이동
        for r, c, num, d in clusters:
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            # 약품이 칠해진 곳에 도착하면 절반 감소 후 방향 변경
            if nr == 0 or nc == 0 or nr == N - 1 or nc == N - 1:
                num //= 2
                d = reverse_dir[d]

            if num > 0:
                new_clusters[(nr, nc)].append((num, d))

        # 합치기
        clusters = []
        for (r, c), group in new_clusters.items():
            if len(group) > 1:
                group.sort(reverse=True)  # 미생물 수가 많은 순으로 정렬
                total_num = sum(num for num, _ in group)
                d = group[0][1]  # 가장 많은 미생물 군집의 방향
                clusters.append((r, c, total_num, d))
            else:
                clusters.append((r, c) + group[0])

    return sum(num for _, _, num, _ in clusters)


T = int(input().strip())  # 테스트 케이스 개수
for t in range(1, T + 1):
    N, M, K = map(int, input().strip().split())
    clusters = [tuple(map(int, input().strip().split())) for _ in range(K)]
    result = simulate_microorganisms(N, M, K, clusters)
    print(f"#{t} {result}")
