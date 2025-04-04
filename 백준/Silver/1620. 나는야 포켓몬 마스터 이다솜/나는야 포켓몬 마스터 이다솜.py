import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N+1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(M):
    poketmon = input().strip()
    if poketmon.isdigit():
        print(num_to_name[int(poketmon)])
    else:
        print(name_to_num[poketmon])
