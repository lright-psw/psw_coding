N = int(input().strip())
members = []

for i in range(N):
    age, name = input().strip().split()
    members.append((i, int(age), name))


members.sort(key=lambda x: (x[1], x[0]))

for i, a, n in members:
    print(f"{a} {n}")
