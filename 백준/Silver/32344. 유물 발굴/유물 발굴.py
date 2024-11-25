r, c = map(int, input().split())
n = int(input())

relic = {}
rst = {}

for _ in range(n):
    a, v, h = map(int, input().split())
    if a not in relic:
        relic[a] = []
    relic[a].append((v, h))

for k, v in relic.items():
    x_coords, y_coords = zip(*v)
    max_x, min_x = max(x_coords), min(x_coords)
    max_y, min_y = max(y_coords), min(y_coords)
    m = (max_x - min_x + 1) * (max_y - min_y + 1)
    rst[k] = m

# 최대 면적과 최소 key를 동시에 계산
max_area = -1
min_key = float('inf')

for k, area in rst.items():
    if area > max_area or (area == max_area and k < min_key):
        max_area = area
        min_key = k

print(f"{min_key} {max_area}")
